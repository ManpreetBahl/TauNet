'''
Copyright (c) 2015 Manpreet Bahl

This file contains the implementation of the
server side of TCP. This allows for user to
recieve messages from multiple clients.

This code was modified from the code found
at:

http://stackoverflow.com/questions/17453212/multi-threaded-tcp-server-in-python

'''

#Import Libraries/Other Files
import socket
import threading
import rc4 
import variables
import datetime

#Server Class
class Server(threading.Thread):

	def __init__(self,clientsocket,clientaddr):
		threading.Thread.__init__(self)
		self.clientsocket = clientsocket
		self.clientaddr = clientaddr

	def run(self):
		while 1:
			data = self.clientsocket.recv(variables.buf) #Recieve data
			if not data: #If empty, break
				break
			#Decrypt data using RC4
			data = rc4.decrypt(data, variables.rounds, variables.key)

			#Determine time that message was received (UTC timezone)
			now = datetime.datetime.now() 
			now = now.strftime("%A, %B %d, %y at %r UTC")
			data = now + '\n' + data
			variables.messages.append(data)
		return

#Server Main
def ServerMain():
	host = ''
	port = 6283 #Set to listen for incoming data on Port 6283
		
	clientaddr = (host,port)

	#Create socket object
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	s.bind(clientaddr)
	threads = []
	
	#Create threads, one for each client that is connected
	while 1:
		s.listen(1)
		clientsocket, clientaddr = s.accept()
		newthread = Server(clientsocket, clientaddr)
		newthread.daemon = True
		newthread.start()
		threads.append(newthread)

	for i in threads:
		i.join()


if __name__ == "__main__":
	ServerMain()

