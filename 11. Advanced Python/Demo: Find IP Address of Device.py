# Code Script 1
from socket import gethostbyname, gethostname
print(gethostbyname(gethostname()))   # 192.168.0.0

# Code Script 2
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])       # 192.168.0.0

