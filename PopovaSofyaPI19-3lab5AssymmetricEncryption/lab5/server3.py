import socket, random, os.path, sys
from multiprocessing import Pool

def logic(K, por):
    
    port = por
    sock = socket.socket()
    sock.bind(('127.0.1.1', port))
    print("port: ", port)

    # while True:
    try:

        sock.listen(10)
        conn, addr = sock.accept()
        data = conn.recv(1024).decode()
        if data.lower() == '':
            sys.exit(0)
            #break
        else:
            print("\nПринятое закодированное сообщение: ", data)
            decoded_str = ch(data, K)
            print("Раскодированное сообщение: ", decoded_str, "\n")
            conn.send(decoded_str.encode())
    except ConnectionResetError:
        pass
    except NameError:
        sock.listen(10)
        conn, addr = sock.accept()
        pass

    #conn.close()

def ch(data, K):
    return "".join(chr(ord(el) - K) for el in data)

def main():
    port = 9090
    sock = socket.socket()
    sock.bind(('localhost', port))
    print("port: ", port)

    if os.path.exists("server3_keys.txt"):
        print("\n***Ключи взяты из файла***")
        with open("server3_keys.txt", "r") as f:
            settings = f.readlines()
        b = int(settings[0].split()[3])
        B = int(settings[1].split()[3])
        g, p, A_b = int(settings[2].split()[3]), int(settings[2].split()[4]), int(settings[2].split()[5])
    else:
        while True:
            try:
                sock.listen(10)
                conn0, addr = sock.accept()

                while True:
                    data = conn0.recv(1024)
                    b = random.randint(0, 10) #закрытый ключ сервера
                    g, p, A_b = [int(el) for el in data.decode().split()] #открытый ключ клиента
                    if g < 0 or p < 0 or A_b < 0:
                        conn0.send("Недопустимый открытый ключ!".encode())
                        sys.exit(0)
                    if not data:
                        break
                    B = g**b % p #открытый ключ сервера
                    conn0.send(str(B).encode())
                    with open("server3_keys.txt", "w", encoding="utf-8") as f:
                        f.write("Закрытый ключ сервера: " + str(b))
                        f.write("\nОткрытый ключ сервера: " + str(B))
                        f.write("\nОткрытый ключ клиента: " + str(g) + " " + str(p) + " " + str(A_b))
                    break
                break
            except ConnectionResetError:
                continue

    print("\033[35m\nЗакрытый ключ сервера: b =", b)
    print("Открытый ключ сервера: B =", B)
    print("Открытый ключ клиента: g =", g, "p =", p, "A_b =", A_b, "\033[0m\n")
    K = A_b**b % p + 1
    print("Общий секретный ключ: K =", K, "\n")

    ports = [i for i in range(9091, 9100)]
    p = Pool(len(ports))
    for por in ports:
        res = p.apply_async(logic, (K, por))
        print(res.get())


if __name__ == "__main__":
    main()