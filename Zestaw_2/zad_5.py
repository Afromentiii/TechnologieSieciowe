import socket

IP_ADDRESS = "127.0.0.1"
PORT = 2901

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
   udp_socket.connect((IP_ADDRESS, PORT))
   
   while True:
       message = input()
       udp_socket.send(bytes(message, "UTF-8"))
       response = udp_socket.recv(1024)
       print(response)
except:
    print("Something went wrong!")
    
udp_socket.close()