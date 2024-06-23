import socket
import threading


def getPeer(server: tuple, name: str) -> tuple:
    """
    Return the other peer infos as tuple while connecting to server
    (IP, PORT, NAME)
    """

    # Sending server infos
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 50001))
    sock.sendto(name.encode(), server)

    # Queuing for datas
    data = sock.recv(1)
    if data == b"1":
        print("[CONSOLE] Connected to server, waiting...\n")

    # Peer datas
    data = sock.recv(128).decode()
    ip, port, name = data.split(":")
    port = int(port)

    print(f"[CONSOLE] Got Peer: \nNAME: {name}\nIP: {ip}\nPORT: {port}\n")

    return ip, port, name


def listenTo(sock, peerName) -> None:
    while True:
        data = sock.recv(128).decode()
        if data == "0":
            print("[CONSOLE] Peer Disconnected\n")
            listener.join()
        print(f"\r[{peerName}] : {data}\n> ", end="")


def talkTo(sock, peerSocket) -> None:
    while True:
        msg = input("> ").encode()
        sock.sendto(msg, peerSocket)
        if msg == "0".encode():
            print("[CONSOLE] Disconnected\n")
            talker.join()



# Getting peer infos
server = ("192.168.1.206", 50002)
# TODO check name length to don't exceed 16bytes
peer = getPeer(server, input("Name: "))
peerSocket = (peer[0], peer[1])
peerName = peer[2]

# Punching hole
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 50001))
sock.sendto(b'1', peerSocket)


listener = threading.Thread(target=listenTo, args=(sock, peerName))
talker = threading.Thread(target=talkTo, args=(sock, peerSocket))
listener.start()
talker.start()