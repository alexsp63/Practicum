from os import name
import socket, random, os.path, sys

def main():
    port = 9090
    print("port: ", port)

    if os.path.exists("client3_keys.txt"):
        print("\n***Ключи взяты из файла***")
        with open("client3_keys.txt", "r") as f:
            settings = f.readlines()
        a_m = int(settings[0].split()[3])
        g, p, A_b = int(settings[1].split()[3]), int(settings[1].split()[4]), int(settings[1].split()[5])
        B = int(settings[2].split()[3])
    else:
        sock = socket.socket()
        sock.connect(('localhost', port))
        a_m = random.randint(0, 10) #закрытый ключ клиента
        g = random.randint(0, 10)
        p = random.randint(1, 10)
        A_b = (g**a_m) % p
        mes = (g, p, A_b) #открытый ключ клиента

        mes_str = " ".join(str(el) for el in mes)

        sock.send(mes_str.encode())

        B = sock.recv(1024).decode()
        try:
            B = int(B)
            with open("client3_keys.txt", "w", encoding="utf-8") as f:
                f.write("Закрытый ключ клиента: " + str(a_m))
                f.write("\nОткрытый ключ клиента: " + str(g) + " " + str(p) + " " + str(A_b))
                f.write("\nОткрытый ключ сервера: " + str(B))
            sock.close()
        except ValueError:
            print(B)
            sys.exit(0)


    def ch(inp):
        return "".join(chr(ord(el) + K) for el in inp)

    print("\033[35m\nЗакрытый ключ клиента: a =", a_m)
    print("Открытый ключ клиента: g =", g, "p =", p, "A_b =", A_b)
    print("Открытый ключ сервера: B =", B, "\033[0m\n")
    K = int(B)**a_m % p + 1
    print("Общий секретный ключ: K =", K, "\n")

    while True:
        port += 1
        sock = socket.socket()
        sock.connect(('127.0.1.1', port))

        print("port: ", port)
        inp = input("\nВведите exit для завершения работы программы или что-либо ещё для шифрования: ")
        if inp.lower() != 'exit':

            mes_str = ch(inp)

            sock.send(mes_str.encode())

            print("\nЗакодированное сообщение: ", mes_str)
            resp = sock.recv(1024).decode()

            print("Раскодированное сообщение: ", resp)
            continue
        else:
            break

    sock.close()

if __name__ == "__main__":
    main()