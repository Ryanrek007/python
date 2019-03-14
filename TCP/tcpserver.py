import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ""
port = 980

socket.bind((address,port))

socket.listen(100)

while True:
    conn, address_client = socket.accept()
    print("Connected to " , address_client)

    data = conn.recv(100)

    data = "Bilang "  + data.decode("ascii")

    conn.send(data.encode("ascii"))
    conn.close()



