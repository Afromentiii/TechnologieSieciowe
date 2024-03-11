import socket

IP_ADDRESS = "127.0.0.1"
PORT = 2907

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    udp_socket.connect((IP_ADDRESS, PORT))
    udp_socket.send(socket.gethostname().encode())
    response = udp_socket.recv(4096)
    print(response.decode())
except:
    print("Something went wrong!")

udp_socket.close()