'''
Copyright (c) 2015 Manpreet Bahl

This file containts the implementaton of the
Linear Linked List. The LLL is used to store 
information about all the contacts and allow 
user to modify the address book.
'''

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

	def add(self, name, ip, port): #Add node to Linked List
		#List is Empty
		if self.head is None: 
			self.head = LinkedList.__Node()
			self.head.set_name(name)
			self.head.set_ip(ip)
			self.head.set_port(port)
			self.head.set_next(None)
			return

		#List is not empty
		#Place node in alphabetical order
		if self.head.get_name() > name: #Check if first node is greater than name to add
			temp = LinkedList.__Node()
			temp.set_name(name)
			temp.set_ip(ip)
			temp.set_port(port)
			temp.set_next(self.head)
			self.head = temp
		else:
			current = self.head #Traverse to the right spot and add node
			while current.has_next():
				if current.get_next().get_name() > name:
					break
				current = current.get_next()
		
			temp = LinkedList.__Node()
			temp.set_name(name)
			temp.set_ip(ip)
			temp.set_port(port)
			temp.set_next(current.get_next())
			current.set_next(temp)
		return

	def display(self): #Display the name of the contacts
		#List is Empty
		if self.head is None:
			print "No Contacts!" 
			return
		
		current = self.head
		num = 1
		while(current): #Traverse and Display
			print str(num) + ") " + "Name: " + current.get_name()
			current = current.get_next()
			num = num + 1
	
	def count(self): #Count number of nodes in Linked List
		#List is empty
		if self.head is None: 
			return 0

		#List is not empty
		current = self.head
		count = 0
		while(current):
			count += 1
			current = current.get_next()
		
		return count		
	
	def delete(self,name): #Delete a node (contact) from Linked List
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

	def search(self,name): #Search for a Contact and return its IP and Port in a 2-Tuple
	
		#List is Empty
		if self.head is None:
			print "No Contacts!"
			return None

		#List is not Empty
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
