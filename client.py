import socket


def getPeer(server: tuple, name: str) -> tuple:
    """
    Return the other peer infos as tuple
    """

    # Sending server infos
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 50001))
    sock.sendto(name.encode(), server)

    # Queuing for datas
    data = sock.recv(1)
    if data == b"1":
        print("[CONSOLE] Connected to server, waiting...")

    # Peer datas
    data = sock.recv(1024).decode()
    ip, port = data.split(":")
    ip = int(ip)
    port = int(port)

    print(f"[CONSOLE] Got Peer: \nIP: {ip}\nPORT: {port}")

    return ip, port


server = ("192.168.1.206", 50002)

#TODO check name length to don't exceed 16bytes
getPeer(server, input("Name: "))


