import socket

port = 50002
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((socket.gethostbyname(socket.gethostname()), port))

print(f"[CONSOLE] Setup completed \nIP: {sock.getsockname()[0]} \nPORT: {sock.getsockname()[1]}")

clients = []

while True:
    data, addr = sock.recvfrom(1)
    print(f"[CONSOLE] Connection From: {addr}")
    clients.append(addr)

    # sending confirmation bit
    sock.sendto(b"1", addr)

    if len(clients) >= 2:
        print(f"[CONSOLE] Got 2 Clients, sending details...")
        break

c1 = clients.pop()
c1Addr, c1Port = c1
c2 = clients.pop()
c2Addr, c2Port = c2

sock.sendto(f"{c1Addr}:{c1Port}".encode(), c2)
sock.sendto(f"{c2Addr}:{c2Port}".encode(), c1)

