import socket

IP_ADDRESS = "127.0.0.1"
PORT = 2906
port_and_adress = (IP_ADDRESS, PORT)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    udp_socket.connect(port_and_adress)
    udp_socket.send(IP_ADDRESS.encode())
    response = udp_socket.recv(4096)
    print(response.decode())
except:
    print("Something went wrong!")

udp_socket.close()