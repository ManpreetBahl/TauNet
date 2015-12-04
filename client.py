'''
Copyright (c) 2015 Manpreet Bahl

This file contains the implemenation of the
client side of TCP. It's used to send messages
to other clients over the Internet

The framework for this code was gotten at:
	https://wiki.python.org/moin/TcpCommunication
'''

#Import Libraries/Other Files
import socket
import rc4
import variables

#Connects and Sends Message to Recipient
def Client(clientsocket,name,host,port,buf):

	host = socket.gethostbyname(host) #Get Host IP/DNS
	clientaddr = (host,port) 

	try:
		clientsocket.connect(clientaddr) #Connect to Recipient's Server
			
		message = MultiLineMessage() #Write Message
		
		#Format data as per TauNet Protocol
		message = "version: {}\r\nfrom: {}\r\nto: {}\r\n\r\n{}\r\n".format(variables.version, variables.username, name, message)

		#Encrypt data usign RC4
		message = rc4.encrypt(message, variables.rounds, variables.key)
		clientsocket.send(message) #Send message
			
	except socket.error: #Failed to connect
		print ("Cannot send message")
	
	clientsocket.close() #Close connection

#Write Message
def MultiLineMessage():
	stop = "stop" #Stop Word when done writing message
	text = []
	print ("Type 'stop' (Case sensitive) to stop writting message")
	print ("Enter Message: ")

	while 1:
		get_input = raw_input()
		if get_input == stop:
			break
		else:
			text.append(get_input)
	
	message = "\r\n".join(text) #Add CR and LF as line ending indicators
	return message

#Creates socket object
def ClientMain(name, host, port):
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	Client(s,name,host,port,variables.buf)
