import socket
import socketserver
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

def get_free_port() :
    with socketserver.TCPServer(("localhost", 0), None) as s:
        free_port = s.server_address[1]
        #print (free_port)
        return free_port

get_free_port()