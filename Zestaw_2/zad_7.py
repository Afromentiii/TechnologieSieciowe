import socket

IP_ADDRESS = "127.0.0.1"
PORT = 80

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    result = udp_socket.connect_ex((IP_ADDRESS, PORT))
    
    if result == 0:
        print("Port is open.")
    else:
        print("Port is not open!")
        exit()
    
    try:
        print(socket.getservbyport(PORT))
    except:
        print("Service's name not found")
except:
    print("Something went wrong!")
    
udp_socket.close()