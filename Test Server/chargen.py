import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 19))

while True:
    data, addr = sock.recvfrom(1024)
    response = ("This the chargen mock server\n").encode()
    sock.sendto(response, addr)
