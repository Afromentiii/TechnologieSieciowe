import ipaddress
import socket

ip_adress = input("Enter IP: ")

try:
    ipaddress.ip_address(ip_adress)
    try:
        print("Hostname adresu: ", ip_adress, " to:", socket.gethostbyaddr(ip_adress)[0])
    except Exception:
        print("Something went wrong")
        
except ValueError:
    print("Adress is not correct.")
    
