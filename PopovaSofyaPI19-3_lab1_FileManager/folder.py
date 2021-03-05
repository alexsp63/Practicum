import os
import shutil
from pathlib import Path

class Folder():

    def __init__(self, name):
            self.name = name

    def show(self, folder):
        '''Показ содержимого каталога'''
        try:
            for el in os.listdir(folder):
                print("\033[34m" + el + "\033[0m")
        except FileNotFoundError:
            print("\033[31mСистеме не удается найти указанный путь!\033[0m")
        except NotADirectoryError:
            print("\033[31mЭто не директория!\033[0m")

    def createdir(self, folder):
        '''Создание папки/каталога'''
        try:
            #если передаётся именно имя папки для создания в текущей директории, а не вложенная несуществующая директория
            os.mkdir(folder)
        except FileNotFoundError:
            os.makedirs(folder)

    def removedir(self, folder):
        '''Удаление папки/каталога'''
        try:
            #папка пустая
            os.rmdir(folder)
        except OSError:
            #папка не пустая
            try:
                shutil.rmtree(folder, ignore_errors=False, onerror=None)
            except FileNotFoundError:
                print("\033[31mНе существует такой папки/директории! Нечего удалять!\033[0m")
        except FileNotFoundError:
            print("\033[31mНе существует такой папки/директории! Нечего удалять!\033[0m")
            
    def go(self, folder):
        '''Переход'''
        try:
            os.chdir(folder)
            self.name = folder
        except FileNotFoundError:
            print("\033[31mНе существует такой папки/директории! Некуда переходить!\033[0m")

    def createfile(self, filename):
        '''Создание пустого файла'''
        Path(filename).touch()

    def write(self, filename, filetext):
        '''Запись/дозапись в файл'''
        try:
            if os.path.exists(self.name + "\\" + filename) or os.path.exists(filename):
                f = open(filename, "a", encoding="utf-8")
                f.write(filetext + "\n")
                f.close()
            else:
                print("\033[31mТакого файла не существует!\033[0m")
        except PermissionError:
            print("\033[31mВы выбрали не файл!\033[0m")
        except FileNotFoundError:
            try:
                f = open(filename, "a", encoding="utf-8")
                f.write(filetext + "\n")
                f.close()
            except FileNotFoundError:
                print("\033[31mТакого файла не существует в данной директории!\033[0m")

    def read(self, filename):
        '''Чтение из файла'''
        try:
            if os.path.exists(self.name + "\\" + filename) or os.path.exists(filename):
                with open(filename, "r") as file:
                    for line in file:
                        print(line, end="")
            else:
                print("\033[31mТакого файла не существует!\033[0m")
        except PermissionError:
            print("\033[31mВы выбрали не файл!\033[0m")
        except FileNotFoundError:
            try:
                with open(self.name + "\\" + filename, "r") as file:
                    for line in file:
                        print(line, end="")
            except FileNotFoundError:
                print("\033[31mТакого файла не существует в данной директории!\033[0m")

    def removefile(self, filename):
        '''Удаление файла'''
        try:
            if os.path.exists(self.name + "\\" + filename) or os.path.exists(filename):
                os.remove(filename)
            else:
                print("\033[31mТакого файла не существует в данной директории!\033[0m")
        except PermissionError:
            print("\033[31mВы выбрали не файл!\033[0m")
        except FileNotFoundError:
            try:
                os.remove(self.name + "\\" + filename)
            except FileNotFoundError:
                print("\033[31mТакого файла не существует в данной директории!\033[0m")

    def copyfile(self, now, new):
        '''Копирование файла'''
        try:
            shutil.copyfile(now, new)
        except FileNotFoundError:
            print("\033[31mНе существует файла, который вы хотите скопировать!\033[0m")

    def movefile(self, now, new):
        '''Перемещение файла'''
        try:
            shutil.move(now, new)
        except FileNotFoundError:
            print("\033[31mНе существует файла, который вы хотите переместить!\033[0m")

    def renamefile(self, old, new):
        '''Переименование файла'''
        try:
            os.rename(old, new)
        except FileNotFoundError:
            print("\033[31mНе существует файла, который вы хотите переименовать!\033[0m")
