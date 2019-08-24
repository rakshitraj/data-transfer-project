import socket
import sys
import csv
import os.path
from time import sleep

filepath = '../record/master_record.csv'

# Initialize csv file with headers
def init_record():
    with open( filepath, 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow([['dataString']])
        #csv_out.writerows([['temp', 'humid', 'a', 'b', 'c', 'sec', 'min', 'hr', 'dd', 'mm', 'yyyy','tzone']])

# Function to record data to csv file
def record(data):

    with open( filepath, 'a+') as out:
        csv_out = csv.writer(out)
        for row in data:
            csv_out.writerow(row)


# Creating server funtion
def server():
    # Create server socket - IPv4 TCP/IP
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind server socket to the address given in command line
    server_name = sys.argv[1]
    server_port = int(sys.argv[2])
    server_address = (server_name, server_port)

    server_sock.bind(server_address)
    print('Starting server at %s port %s' %server_address)

    server_sock.listen(5)

    while True:
        print('\n...waiting for connection...')
        client_sock, client_addr = server_sock.accept()
        try:
            print('\nclient connected: ', client_addr)
            while True:
                data = (client_sock.recv(1024)).decode("unicode-escape")
                print('Received: "%s"' %data)
                if data:
                    record([[data]])
                else:
                    print('NO TRANSMISSION')
                    break
        finally:
            client_sock.close()

def main():
    if not (os.path.isfile(filepath)):
        init_record()
    server()

main()
