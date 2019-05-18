import socket
from tile import sleep

def client_app():

    client = socket.socket(AF_INET, socket.SOCK_STREAM)

    server_hostname = sys.argv[1]
    server_port = int(sys.argv[2])
    server_address = (server_address, server_port)

    client.connect(server_address)

    while True:
        try
