import socket

def getPeer(server):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 50001))
    sock.sendto(b"0",server)

    while True:
        data = sock.recv(1)
        if data == 1:
            print("[CONSOLE] Connected to server, waiting...")
            break

    data = sock.recv(1024).decode()
    ip, port = data.split(":")
    ip = int(ip)
    port = int(port)

    print(f"[CONSOLE] Got Peer: \nIP: {ip}\nPORT: {port}")


server = (socket.gethostbyname(socket.gethostname()), 50002)
getPeer(server)