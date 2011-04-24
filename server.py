# SBHS Server
# ===========

import sbhs_dummy as sbhs
# import sbhs
import json
import socket

WhichBoard = 0
PORT = 5000

def serve(WhichBoard, PORT):
        ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ServerSocket.bind(("", PORT))
	ServerSocket.listen(5)
	
	ClientSocket, ClientAddress = ServerSocket.accept()
	print "Got Connection from ", ClientAddress
	print "Attempting to connect to ", WhichBoard
	try:
		sbhs.start(WhichBoard)
	except:
		print "Unable to connect to board ", WhichBoard
		ClientSocket.send("Unable to connect to board")
		ClientSocket.close()
		return 0

	while True:
		ClientDataString = ClientSocket.recv(512)
		print "Got data:\n", ClientDataString
		 
		# The above markup is to be in JSON. 
		ClientData  = json.loads(ClientDataString) # If error, try/except
		print "Understood data as:\n", type(ClientData), "\n", ClientData
		# heatForSBHS = ClientData['heat']
		# fanForSBHS  = ClientData['fan']
		if 'heat' in ClientData:
			print "Got heat"
			sbhs.heat(ClientData['heat'], WhichBoard)
		if 'fan' in ClientData:
			print "Got fan"
			sbhs.fan(ClientData['fan'], WhichBoard)
		SBHSTemperature = sbhs.temp(WhichBoard)
		
		ClientSocket.send(json.dumps({"temp": SBHSTemperature}))
		if 'quit' in ClientData:
			print "Wrapping up"
			sbhs.finish(WhichBoard)
			break
	ClientSocket.close()
	ServerSocket.close()
	return 1
