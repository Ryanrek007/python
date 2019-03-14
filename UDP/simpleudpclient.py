#inisialisais socket
import socket

#inisialiasi objek socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

MAX_SIZE = 65536

data = "Hai"
print ('Address before sending:')

sock.sendto(data.encode('ascii'),("127.0.0.1", 690))

data = sock.recv(MAX_SIZE)

print(data)