#inisialisai socket
import socket

#inisialisai objek socket
sock =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MAX_SIZE = 80

sock.bind(("0.0.0.0",690))

while True:
    data, addr = sock.recvfrom(MAX_SIZE)

    data ="ok " +  data.decode("ascii")

    sock.sendto(data.encode("ascii"), addr)

