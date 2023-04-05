import socket
from requests import get

def get_ip_localhost() :
    print (socket.gethostbyname(socket.gethostname()))


def get_ip_public() :
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip))    
    

def get_ip() :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = (s.getsockname()[0])
    s.close()
    #print (ip)
    return ip

get_ip()    #equivalent du ifconfig -a