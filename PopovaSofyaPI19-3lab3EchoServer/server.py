import socket, threading, queue, random

def RecvData(sock,recvPackets):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            recvPackets.put((data,addr))
            print(data, addr)
        except ConnectionResetError:
            continue

def sending(c):
    HEADERSIZE = 3
    name = len(data.split(":")[0]) + 2
    message = data.encode("utf-8")
    really_len = len(message) - len("\nEnter your message:\n") - name
    if really_len >= 0:
        message = f"{really_len:<{HEADERSIZE}}".encode("utf-8") + message
        s.sendto(bytes(message), c)


logs = ""
f = open("ServerLogs.txt", "w")
f.close()
host = socket.gethostbyname(socket.gethostname())
print('\033[33mServer is working on IP -> \033[0m'+str(host))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
logs += "Server is active\n"
port = 5000
try:
    s.bind((host, port))
except OSError:
    port = random.randint(5000, 20000)
print("\033[33mServer is using port -> \033[0m" +str(port))
f = open("serverPort.txt", "w")
f.write(str(host) + "\n")
f.write(str(port))
f.close()
logs += "Port is listened\n"
clients = set()
recvPackets = queue.Queue()

print('Server is running...')

f = open("ServerLogs.txt", "a")
f.write(logs)
f.close()

threading.Thread(target=RecvData,args=(s,recvPackets)).start()

while True:
    while not recvPackets.empty():
        data, addr = recvPackets.get()
        if addr not in clients:
            clients.add(addr)
            logs = "Client is connected\n"
            f = open("ServerLogs.txt", "a")
            f.write(logs)
            f.close()
            continue
        clients.add(addr)
        logs = "Client is listened\n"
        f = open("ServerLogs.txt", "a")
        f.write(logs)
        f.close()
        data = data.decode('utf-8') + "\033[35m\n Enter your message:\n\033[0m"
        if data.endswith('exit'):
            clients.remove(addr)
            continue
        print(str(addr)+data)
        for c in clients:
            if c!=addr:
                sending(c)
                logs = "Data is sent to a client\n"
                f = open("ServerLogs.txt", "a")
                f.write(logs)
                f.close()
s.close()