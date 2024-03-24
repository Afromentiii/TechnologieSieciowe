import socket
import datetime

IP_ADDRESS = "127.0.0.1"
PORT = 8000

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind((IP_ADDRESS, PORT))

while True:
     data1, addr = udp_server_socket.recvfrom(1024)
     data2, addr = udp_server_socket.recvfrom(1024)
     data3, addr = udp_server_socket.recvfrom(1024)

     if data1 and data2 and data3:
        score = float()
        print(data1.decode(),data2.decode(),data3.decode())

        if data2.decode() == "+":
            score = float(data1.decode()) + float(data3.decode())
        elif data2.decode() == "-":
            score = float(data1.decode()) - float(data3.decode())
        elif data2.decode() == "*":
            score = float(data1.decode()) * float(data3.decode())
        elif data2.decode() == "/":
            score = float(data1.decode()) / float(data3.decode())

        udp_server_socket.sendto(str(score).encode(),addr)
