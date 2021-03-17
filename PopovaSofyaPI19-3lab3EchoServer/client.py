import socket, threading, os

def ReceiveData(sock):
    while True:
        try:
            HEADERSIZE = 3
            data, addr = sock.recvfrom(1024)
            true_data = data[HEADERSIZE:]
            print(true_data.decode('utf-8'))
        except:
            pass

host = ""
port = ""

while True:
    try:
        if host == "" and port == "":
            while True:
                try:
                    host = input("\033[34mEnter your hostname -> \033[0m")
                    port = int(input("\033[34mEnter your port -> \033[0m"))
                    break
                except (ValueError, TypeError):
                    print("\033[31mInvalid port!\033[0m")
                    continue
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print('\033[33mClient IP -> \033[0m' + str(host) + '\033[33m Port -> \033[0m' + str(port))

        with open("serverPort.txt", "r") as f:
            settings = f.read().splitlines()

        serverIP = settings[0]
        serverPort = int(settings[1])
        # serverIP = input("Enter Server IP -> ")
        # serverPort = int(input("Enter Server Port -> "))

        f.close()
        server = (str(serverIP), serverPort)
        s.sendto("just for exception".encode("utf-8"), server)

        list_of_clients = {}
        if os.path.exists("clients.txt") == False:
            clients = open("clients.txt", "w")

        with open("clients.txt", "r") as clients:
            records = clients.read().splitlines()

        for line in records:
            record = line.split(";")
            list_of_clients[record[0]] = [record[1], record[2]]

        if host in list_of_clients:
            name = list_of_clients[host][0]
            while True:
                password = input("\033[34mEnter your password: \033[0m")
                if password == list_of_clients[host][1]:
                    print("\033[32mHELLO,", name + "\033[0m")
                    break
                else:
                    print("\033[31mWrong password!\033[0m")
                    continue
        else:
            name = input('\033[34mPlease enter your name here: \033[0m')
            password = input("\033[34mPlease think of a password: \033[0m")
            print("\033[32m" + name + ", you were added to clients list\033[0m")
            clients = open("clients.txt", "a")
            clients.write(str(host) + ";" + str(name) + ";" + str(password) + "\n")
            clients.close()

        s.sendto(name.encode('utf-8'), server)
        threading.Thread(target=ReceiveData,args=(s,)).start()
        while True:
            print("\033[35m\n Enter your message:\n \033[0m")
            data = input()
            if data == 'exit':
                logs = "Connection with the client is closed\n"
                f = open("ServerLogs.txt", "a")
                f.write(logs)
                f.close()
                s.close()
                os._exit(0)
                break
            elif data=='':
                continue
            data = '<'+name+'>: '+ data
            s.sendto(data.encode('utf-8'),server)

    except OSError as e:
        print(e)
        print("\033[31mWrong server IP! Try again!\033[0m")
        continue
    except (ValueError, TypeError) as e:
        print(e)
        continue


s.close()