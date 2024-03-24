import socket
import datetime

IP_ADDRESS = "127.0.0.1"
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP_ADDRESS, PORT))
server_socket.listen(1)

while True:
     conn, addr = server_socket.accept()
     data = conn.recv(1024)

     if data:
         current_time = datetime.datetime.now()
         print('Recived:', data.decode())
         conn.sendall(data)