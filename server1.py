import socket, time

host = socket.gethostbyname(socket.gethostname())
port = 9090


clients1 = []
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))



quit = False
print("[ Server Started ]")

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients1:
            clients1.append(addr)

        itsatime = time.strptime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
        print(data.decode("utf-8"))

        for client1 in clients1:
            if addr in client1:
                s.sendto(data,client1)
    except:
        print("\n[ Server Stopped ]")
        quit = True

s.close()
