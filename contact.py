class LinkedList:
	
	class __Node:
		def __init__(self):
			self.name = None
			self.ip = None
			self.port = None
			self.next = None
		
		def set_next(self,new_next):
			self.next = new_next
		
		def get_next(self):
			return self.next
		
		def has_next(self):
			return self.next != None
		
		def set_name(self, name):
			self.name = name
		
		def get_name(self):
			return self.name
		
		def set_ip(self, ip):
			self.ip = ip
		
		def get_ip(self):
			return self.ip
		
		def set_port(self, port):
			self.port = port
		
		def get_port(self):
			return self.port
			
	def __init__(self):
		self.head = None

	def add(self, name, ip, port):
		#List is Empty
		if self.head is None: 
			self.head = LinkedList.__Node()
			self.head.set_name(name)
			self.head.set_ip(ip)
			self.head.set_port(port)
			self.head.set_next(None)
			return

		#List has nodes
	
		#Check if first node is greater than name to add
		if self.head.get_name() > name:
			temp = LinkedList.__Node()
			temp.set_name(name)
			temp.set_ip(ip)
			temp.set_port(port)
			temp.set_next(self.head)
			self.head = temp
		else:
			current = self.head
			while current.has_next():
				if current.get_next().get_name() > name:
					break
				current = current.get_next()
		
			temp = LinkedList.__Node()   #(name,ip,port)
			temp.set_name(name)
			temp.set_ip(ip)
			temp.set_port(port)
			temp.set_next(current.get_next())
			current.set_next(temp)
		return

	def display(self):
		#List is Empty
		if self.head is None:
			print "No Contacts!" 
			return
		
		current = self.head
		num = 1
		while(current):
			print str(num) + ") " + "Name: " + current.get_name()
			current = current.get_next()
			num = num + 1
	
	def count(self):
		if self.head is None:
			return 0
		current = self.head
		count = 0
		while(current):
			count += 1
			current = current.get_next()
		
		return count		
	
	def delete(self,name):
		current = self.head
		previous = None
		match = False
	
		while(current and match is False):
			if current.get_name() == name:
				match = True
			else:
				previous = current
				current = current.get_next()
		
		if current is None:
			print "Contact not in List!"
		
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def search(self,name):
	
		if self.head is None:
			print "No Contacts!"
			return None

		current = self.head
		found = False
		while(current and found is False):
			if current.get_name() == name:
				found = True
			else:
				current = current.get_next()
		
		if found == True:
			return (current.get_ip(), current.get_port())
		
		if found == False:
			print "Contact was not Found!"
			return None
'''
def ContactMain():	
	AddressBook = LinkedList()
	f = open("TauNet User and Hostnames - User and Hostnames.csv")
	
	try:
		reader = csv.reader(f)
		for i in range(2):
			next(reader,None)
		
		for row in reader:
			if row[0] == "":
				f.close()
				break

			AddressBook.add(row[0], row[1], int(row[2]))
	finally:
		f.close()

	#print "Linked List"
	#AddressBook.display()

if __name__ == "__main__":
	ContactMain()
'''

'''
def main():
	test = LinkedList()

	for i in range(0,5):
		name = raw_input("Enter Name: ")
		ip = raw_input("Enter IP: ")
		port = int(raw_input("Enter Port: "))
		test.add(name, ip, port) 
	
	test.display()
	number = test.count()
	
	print "Number of Nodes: %d" %number

	to_find = raw_input("Enter Name to Find: ")
	found_ip, found_port = test.search(to_find)

	print "Ip Found: " + found_ip
	print "Port Found: %d" %found_port
	
main()
'''
