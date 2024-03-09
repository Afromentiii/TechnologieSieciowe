import ntplib
from datetime import datetime

IP_ADDRESS = "zegar.umk.pl"
client = ntplib.NTPClient()

try:
    resp = client.request(IP_ADDRESS)
    print(datetime.fromtimestamp(resp.orig_timestamp).strftime('%Y-%m-%d %H:%M:%S'))
except:
    print("Connection error!")


