import socket
import ipaddress

def checkPort(port : int) -> bool:
    if port < 0 or port > 65535:
        print("Bad port number.")
        return False
    return True    

def checkIP(ip) -> bool:
    ipv4_test : bool
    hostname_test : bool
    
    try:
        ipaddress.ip_address(ip)
        ipv4_test = True
    except ValueError:
        ipv4_test = False
        
    try:
        socket.gethostbyaddr(ip)[0]
        hostname_test = True
    except Exception:
        hostname_test = False
        
    if ipv4_test or hostname_test:
        return True
    else:
        return False

ip = input("Enter ip: ")
port = int(input("Enter port:"))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if checkIP(ip) and checkPort(port):
    print("Port and IP/Hostname is correct")
    try:
        s.connect((ip, port))
        print("Connect to", ip, " ", port, " is successful.")
    except:
        print("Connect error.")
else:
    print("Something went wrong")

s.close()