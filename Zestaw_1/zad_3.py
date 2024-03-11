import ipaddress

ip_adress = input("Enter IP: ")

try:
    ipaddress.ip_address(ip_adress)
    print("Adress is correct.")
    
except ValueError:
    print("Adress is not correct.")