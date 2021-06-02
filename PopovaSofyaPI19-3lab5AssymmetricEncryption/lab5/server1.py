import socket, random

sock = socket.socket()
sock.bind(('localhost', 9090))

while True:
    try:
        sock.listen(10)
        conn, addr = sock.accept()

        while True:
            data = conn.recv(1024)
            if data.decode().lower() == '':
                break
            else:
                b = random.randint(0, 10)
                print("Сгенерированные данные:\n b =", b, "\n")
                g, p, A_b = [int(el) for el in data.decode().split()]
                print("Полученные данные:\n g =", g, "p =", p, "A =", A_b, "\n")
                if not data:
                    break
                K = A_b**b % p
                B = g**b % p
                print("Отправляемые данные:\n B =", B, "\n")
                print("\033[33mK =", K, "\033[0m\n")
                conn.send(str(B).encode())
    except ConnectionResetError:
        continue

conn.close()