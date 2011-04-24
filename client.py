import socket
import json
import time

PORT = 5000
IPADDRESS = "localhost"

def connect(IPADDRESS, PORT):
	ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ClientSocket.connect((IPADDRESS, PORT))
	while True: 
		data=raw_input("Enter JSON data to send\n-->")
		if (data == 'q') or (data == 'quit'):
			print "Quitting"
			ClientSocket.send('{"quit": true}')
			break
		else:
			ClientSocket.send(data)
	time.sleep(0.1)
	ClientSocket.close()
