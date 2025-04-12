from osc import *
import socket

#socket information for a UDP client connection for MAX/MSP
IP = "localhost"
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#creates an OSC message off a list of float data and sends it over the port and ip of the UDP server in MAX.
def send(floats):
    client.sendto(create_message(floats), (IP, PORT))
