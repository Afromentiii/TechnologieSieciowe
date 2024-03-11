import socket

hostname = input("Enter hostname: ")

try:
    ipv4 = socket.gethostbyname(hostname)
    print("Adres IP dla hosta:", hostname, " to", ipv4)
except:
    print("Hostname is wrong.")
    
