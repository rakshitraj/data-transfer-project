import socket
import sys
from tile import sleep

def client_app():

    client = socket.socket(AF_INET, socket.SOCK_STREAM)

    server_hostname = sys.argv[1]
    server_port = int(sys.argv[2])
    server_address = (server_address, server_port)

    if(client.connect(server_address))
        print("Connected to #dataserver")

    while True:
        try:
            data = s.recv(1024).decode()
            print("Received:")
            print(data)
        finally:
            pass

client_app()
