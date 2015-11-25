version = raw_input('Enter Version Number: ').decode('utf-8')
recipient = raw_input('To: ').decode('utf-8')
sender = raw_input('From: ').decode('utf-8')
message = raw_input('Message: ').decode('utf-8')

class Node(object)
{
	def __init___(self, name, ip, port, key, next):
		self.name = name
		self.ip = ip
		self.port = port
		self.key = key
		self.next = next

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next
	
	def get_name(self):
		return self.name
}

class LinkedList(object)
{
	def __init__(self):
		self.head = head


}


'''
def whatisthis(message):
	if isinstance(message, str):
		print "Ordinary String"
	elif isinstance(message, unicode):
		print "Unicode String"
	else:
		print "Not a String"
	return


whatisthis(version)
whatisthis(recipient)
whatisthis(sender)
whatisthis(message)
'''
