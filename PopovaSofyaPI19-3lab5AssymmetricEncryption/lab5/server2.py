import socket, random

sock = socket.socket()
sock.bind(('localhost', 9090))

while True:
    try:
        sock.listen(10)
        conn, addr = sock.accept()

        while True:
            data = conn.recv(1024)
            b = random.randint(0, 10) #закрытый ключ сервера
            g, p, A_b = [int(el) for el in data.decode().split()] #открытый ключ клиента
            if not data:
                break
            B = g**b % p #открытый ключ сервера
            conn.send(str(B).encode())
            break
        break
    except ConnectionResetError:
        continue

print("\033[35m\nЗакрытый ключ сервера: b =", b)
print("Открытый ключ сервера: B =", B)
print("Открытый ключ клиента: g =", g, "p =", p, "A_b =", A_b, "\033[0m\n")
K = A_b**b % p + 1
print("Общий секретный ключ: K =", K, "\n")

while True:
    try:

        data = conn.recv(1024).decode()
        if data.lower() == '':
            break
        else:
            print("\nПринятое закодированное сообщение: ", data)
            decoded_str = "".join(chr(ord(el) - K) for el in data)
            print("Раскодированное сообщение: ", decoded_str, "\n")
            conn.send(decoded_str.encode())
    except ConnectionResetError:
        continue

conn.close()