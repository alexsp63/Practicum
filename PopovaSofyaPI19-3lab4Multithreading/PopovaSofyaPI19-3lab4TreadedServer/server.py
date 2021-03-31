import socket, threading, queue, random

def RecvData(sock,recvPackets):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            recvPackets.put((data,addr))
            print(data, addr)
        except ConnectionResetError:
            continue


host = socket.gethostbyname(socket.gethostname())
print('\033[33mServer is working on IP -> \033[0m'+str(host))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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

clients = set()
recvPackets = queue.Queue()

threading.Thread(target=RecvData,args=(s,recvPackets)).start()

while True:

    while not recvPackets.empty():
        data, addr = recvPackets.get()
        if addr not in clients:
            clients.add(addr)
            continue
        #clients.add(addr)

        data = data.decode('utf-8') + "\033[35m\n Enter your message:\n\033[0m"
        if data.endswith('exit'):
            clients.remove(addr)
            continue

s.close()