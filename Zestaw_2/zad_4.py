import socket

IP_ADDRESS = "127.0.0.1"
PORT = 2901
message = "Hello there young jedi!"

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
   udp_socket.connect((IP_ADDRESS, PORT))
   udp_socket.send(bytes(message,"UTF-8"))
   print("Message sent.")
except:
    print("Something went wrong!")