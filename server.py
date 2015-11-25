import socket
import threading
import rc4 
import variables
import datetime

class Server(threading.Thread):

	def __init__(self,clientsocket,clientaddr):
		threading.Thread.__init__(self)
		self.clientsocket = clientsocket
		self.clientaddr = clientaddr

	def run(self):
		while 1:
			data = self.clientsocket.recv(variables.Buf)
			if not data:
				break
			data = rc4.decrypt(data, variables.Rounds, variables.Key)

			now = datetime.datetime.now()
			now = now.strftime("%A, %B %d, %y at %r UTC")
			data = now + '\n' + data
			variables.messages.append(data)
		return

def ServerMain():
	host = ''
	port = 6283
		
	clientaddr = (host,port)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	s.bind(clientaddr)
	threads = []

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

