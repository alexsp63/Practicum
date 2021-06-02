import socket, random

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    inp = input("\nВведите exit для завершения работы программы или что-либо ещё для продолжения работы: ")
    if inp.lower() != 'exit':
        a_m = random.randint(0, 10)
        g = random.randint(0, 10)
        p = random.randint(1, 10)
        print("Сгенерированные данные:\n a =", a_m, "\n")
        A_b = (g**a_m) % p
        mes = (g, p, A_b)

        mes_str = " ".join(str(el) for el in mes)

        sock.send(mes_str.encode())

        print("Отправляемые данные:\n g =", g, "p =", p, "A =", A_b, "\n")
        B = sock.recv(1024).decode()

        print("Полученные данные: \nB =", B, "\n")
        K = int(B)**a_m % p
        print("\033[33mK =", K, "\033[0m")
        continue
    else:
        break

sock.close()
