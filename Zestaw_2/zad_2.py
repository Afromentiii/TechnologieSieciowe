import socket

IP_ADDRESS = "127.0.0.1"
PORT = 2900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((IP_ADDRESS, PORT))
    sock.settimeout(5)
    sock.send(b"Hello there!")

    data = sock.recv(1024)
    print("Data received from", IP_ADDRESS, "is:", data.decode())
except:
    print("Connection error!")

sock.close()