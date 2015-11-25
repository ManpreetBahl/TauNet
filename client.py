import socket
import rc4
import variables

Username = "Manpreet"
Version = "0.2"

def Client(clientsocket,name,host,port,buf):

	global Username
	global Version

	host = socket.gethostbyname(host)
	clientaddr = (host,port)

	try:
		clientsocket.connect(clientaddr)
		while 1:
			print ("Type bye to cancel message")
			message = raw_input("Enter Message: ")
		
			if message == "bye":
				break
		
			message = "Version:{}\nFrom:{}\nTo:{}\nMessage:{}\n".format(Version,Username, name, message)

			message = rc4.encrypt(message, variables.Rounds, variables.Key)
			clientsocket.send(message)
	except socket.error:
		print ("Cannot send message")
	
	clientsocket.close()

def ClientMain(name, host, port):
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	Client(s,name,host,port,variables.Buf)

'''
if __name__ == "__main__":
	ClientMain(name, host, port)
'''
