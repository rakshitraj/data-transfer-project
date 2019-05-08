import serial
import socket, sys
import struct
from time import sleep

FORMAT = '%H %M %S %d %m %Y %Z'
SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_RATE = 9600

# function to read the serial output and return it
def serial_reading():

    ser = serial.Serial(
        port=SERIAL_PORT,
        baudrate = SERIAL_RATE,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    line = ser.readline().strip()
    timestamp = add_timestamp()
    line = line + ' ' + add_timestamp()
    ser.close()

    sleep(2)
    print line
    return line

# Function that delivers the timestamp
def add_timestamp():
    return str(time.strftime(FORMAT,time.localtime()))

def client_app():

    # Create client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to entered sever address
    server_hostname = sys.argv[1]
    server_port = int(sys.argv[2])
    server_address = (server_hostname, server_port)

    client.connect(server_address)

    #client.sendall('...handshake acknowledged...')

    while True:
        try:
            data_string = serial_reading()
            if data_string :
                client.sendall(data_string)
            else:
                continue
        finally:
            pass

def main():
    client_app()

main()
