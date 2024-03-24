import socket
import datetime

IP_ADDRESS = "127.0.0.1"
PORT = 8000

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind((IP_ADDRESS, PORT))

while True:
     data, addr = udp_server_socket.recvfrom(1024)

     if data:
        try:
            hostname, _, _ = socket.gethostbyaddr(data.decode())
            udp_server_socket.sendto(hostname.encode(), addr)
        except socket.herror:
            udp_server_socket.sendto(b"Bad address!", addr)
            print("Bad address!")

