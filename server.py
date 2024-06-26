import socket

port = 50002
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((socket.gethostbyname(socket.gethostname()), port))

print(f"[red][CONSOLE] Setup completed: \nIP: {sock.getsockname()[0]} \nPORT: {sock.getsockname()[1]}\n")

clients = []

while True:
    # Receiving datas
    data, addr = sock.recvfrom(16)
    print(f"[CONSOLE] Connection From: \n{addr[0]}\n{data.decode()}\n")
    clients.append((addr, data.decode()))

    # Sending confirmation bit
    sock.sendto(b"1", addr)

    if len(clients) >= 2:
        print(f"[CONSOLE] Got 2 Clients, sending details...")
        break

c1 = clients.pop()
c1Addr, c1Port = c1[0]
c1Name = c1[1]
c2 = clients.pop()
c2Addr, c2Port = c2[0]
c2Name = c2[1]

sock.sendto(f"{c1Addr}:{c1Port}:{c1Name}".encode(), c2[0])
sock.sendto(f"{c2Addr}:{c2Port}:{c2Name}".encode(), c1[0])

