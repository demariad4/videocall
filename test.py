import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9999))
print(socket.gethostbyname(socket.gethostname()))
data = sock.recvfrom(1024)
print("cia")
print(data)
