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
			
		message = MultiLineMessage()
		pdb.set_trace()	
		message = "Version:{}\r\nFrom:{}\r\nTo:{}\r\n{}\r\n".format(Version,Username, name, message)

		message = rc4.encrypt(message, variables.Rounds, variables.Key)
		clientsocket.send(message)
			
	except socket.error:
		print ("Cannot send message")
	
	clientsocket.close()

def MultiLineMessage():
	stop = "stop"
	text = []
	print ("Type 'stop' (Case sensitive) to stop writting message")
	print ("Enter Message: ")

	while 1:
		get_input = raw_input()
		if get_input == stop:
			break
		else:
			text.append('\t' + get_input)
	
	message = "\r\n".join(text)
	return message

def ClientMain(name, host, port):
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	Client(s,name,host,port,variables.Buf)
