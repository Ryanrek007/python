import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address =  "127.0.0.1"
port =  980

socket.connect((address,port))
print("CONNECTING to ... " + address)

print("PROGRAM KONEKSI CLIENT-SERVER SEDERHANA")
data =  input("Masukkan payload message: ")
socket.send(data.encode("ascii"))

data = socket.recv(100)
print(data.decode("ascii"))

