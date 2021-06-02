"""
/users - данные о всех юзерах
/regs - регистрация
/users/login - информация о юзере по логину
"""

from flask import Flask, request, jsonify
import sqlite3
from hashlib import md5
from datetime import datetime
from typing import Union

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def _help() -> str:
    """
    Запуск приветственной страницы
    """
    with open('welcome.html', 'r', encoding='utf-8') as f:
        return f.read()

def _register(json: dict) -> Union[dict, tuple]:
    """
    Регистрация при успешной проверке данных для регистрации
    """
    with sqlite3.connect('Users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT login FROM users WHERE login = ?", (json.get('login', ''),))
        selected = cursor.fetchone()
        if selected:
            return {'status': 'user already exists'}, 403
        dt = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        _hash = md5("".join((json.get('login', ''), json.get('password', ''))).encode()).hexdigest()
        cursor.execute(f'INSERT INTO users VALUES (?, ?, ?)', (json.get('login', ''), _hash, dt))
        return {'status': 'success', 'datetime': dt}


@app.route('/reg', methods=['POST', "GET"])
def register() -> Union[dict, tuple]:
    """
    Проверка данных, поступающих на регистрацию
    """
    print(request.json)
    if request.json is None or not all([x in request.json for x in ('login', 'password')]):
        return {'status': 'bad request'}, 400
    return _register(request.json)


@app.route('/users/<string:login>', methods=['GET'])
def get_user_by_login(login: str) -> Union[dict, tuple]:
    """
    Получение пользователя по логину
    """
    with sqlite3.connect('Users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE login = ?', (login,))
        selected = cursor.fetchone()
        if selected is None:
            return {'status': 'not found'}, 404
        return dict(zip(('login', 'hash_password', 'reg_date'), selected))


@app.route('/users', methods=['GET'])
def get_all_users() -> list:
    """
    Получение всех пользователей
    """
    with sqlite3.connect('Users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        return jsonify([dict(zip(('login', 'hash_password', 'reg_date'), x)) for x in cursor.fetchall()])

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
