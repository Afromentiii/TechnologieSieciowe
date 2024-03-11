import socket

IP_ADDRESS = "127.0.0.1"
PORT = 2902

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

number_1 = float(input())
operator = input()
number_2 = float(input())

try:
    udp_socket.connect((IP_ADDRESS, PORT))
    
    udp_socket.send(bytes(str(number_1), "UTF-8"))
    udp_socket.send(operator.encode())
    udp_socket.send(bytes(str(number_2), "UTF-8"))
    
    response = udp_socket.recv(4096)
    print(response.decode())
except:
    print("Something went wrong!")
    
udp_socket.close()