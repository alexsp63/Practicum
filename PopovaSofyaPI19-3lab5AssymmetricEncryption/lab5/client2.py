import socket, random

sock = socket.socket()
sock.connect(('localhost', 9090))


a_m = random.randint(0, 10) #закрытый ключ клиента
g = random.randint(0, 10)
p = random.randint(1, 10)
A_b = (g**a_m) % p
mes = (g, p, A_b) #открытый ключ клиента

mes_str = " ".join(str(el) for el in mes)

sock.send(mes_str.encode())

B = sock.recv(1024).decode()

print("\033[35m\nЗакрытый ключ клиента: a =", a_m)
print("Открытый ключ клиента: g =", g, "p =", p, "A_b =", A_b)
print("Открытый ключ сервера: B =", B, "\033[0m\n")
K = int(B)**a_m % p + 1
print("Общий секретный ключ: K =", K, "\n")

while True:
    inp = input("\nВведите exit для завершения работы программы или что-либо ещё для шифрования: ")
    if inp.lower() != 'exit':
        A_b = (g**a_m) % p
        mes = (g, p, A_b)

        mes_str = "".join(chr(ord(el) + K) for el in inp)

        sock.send(mes_str.encode())

        print("\nЗакодированное сообщение: ", mes_str)
        resp = sock.recv(1024).decode()

        print("Раскодированное сообщение: ", resp)
        continue
    else:
        break

sock.close()
