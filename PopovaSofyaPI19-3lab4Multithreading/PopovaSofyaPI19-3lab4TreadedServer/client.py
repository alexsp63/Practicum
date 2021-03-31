import socket, threading, os, random

def ReceiveData(sock):
    while True:
        try:
            HEADERSIZE = 3
            data, addr = sock.recvfrom(1024)
            true_data = data[HEADERSIZE:]
            print(true_data.decode('utf-8'))
        except:
            pass

while True:

    host = socket.gethostbyname(socket.gethostname())
    port = random.randint(6000,10000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('\033[33mClient IP -> \033[0m' + str(host) + '\033[33m Port -> \033[0m' + str(port))

    with open("serverPort.txt", "r") as f:
        settings = f.read().splitlines()

    serverIP = settings[0]
    serverPort = int(settings[1])

    server = (str(serverIP), serverPort)
    #s.sendto("just for exception".encode("utf-8"), server)

    s.sendto(host.encode('utf-8'), server)
    threading.Thread(target=ReceiveData,args=(s,)).start()
    while True:
        print("\033[35m\n Enter your message:\n \033[0m")
        data = input()
        if data == 'exit':
            os._exit(0)
            break
        elif data=='':
            continue
        data = '<'+host+'>: '+ data
        s.sendto(data.encode('utf-8'),server)


s.close()