import server
import client
import contact
import threading
import variables
import sys
import csv
import os

def Server():	
	server.ServerMain()

def LoadContacts():
	AddressBook = contact.LinkedList()
	f = open("TauNet User and Hostnames - User and Hostnames.csv")
	
	try:
		reader = csv.reader(f)
		next(reader,None)
		
		encryption_key = reader.next()
		variables.Key = encryption_key[0]	

		for row in reader:
			if row[0] == "":
				f.close()
				break

			AddressBook.add(row[0], row[1], int(row[2]))
	finally:
		f.close()

	return AddressBook

def SaveMessageHistory():
	
	f = open("Message History.csv", "a")

	try:
		f.write("\n".join(variables.messages))

	finally:
		f.close()

def GoAgain(choice):
	while True:
		if choice == 2:
			again = raw_input("Send Message to Another Client? [Y/N]: ")
			againUpper = again.upper()
		
		if choice == 4:
			again = raw_input("Add another contact? [Y/N]: ")
			againUpper = again.upper()
	
		if choice == 5:
			again = raw_input("Delete another contact? [Y/N]: ")
			againUpper = again.upper()

		if len(againUpper) == 1:
			break
		print ("Please enter Y for Yes or N for No (case insensitive)")
	
	if againUpper == "Y":
		return True
	else:
		return False

def Menu():

	AddressBook = LoadContacts()

	choice = 0
	
	while choice != 8:	
		print("\n")
		print("----------MENU----------")
		print("1) View Messages (Current Session)")
		print("2) Send Messages")
		print("3) View Message History (Previous Sessions)")
		print("4) Delete Message History (Previous Sessions)")
		print("5) View Contacts")
		print("6) Add Contact")
		print("7) Remove Contact")
		print("8) Quit")
		print("------------------------") 
		print("\n")
		choice = input("Enter Choice: ")
	
		if choice == 1:
			temp = os.system("clear")
			variables.display()

		elif choice == 2:
			temp = os.system("clear")
			again = True

			while again is True:			
				recipient = raw_input("Enter Recipient Name: ")
				address = AddressBook.search(recipient)
				if address is not None:
					host, port = address
					client.ClientMain(recipient,host,port)
					
				again = GoAgain(choice)

		elif choice == 3:

			try:
				f = open("Message History.csv")	
				reader = csv.reader(f)
				for row in reader:
					print ''.join(row)
				f.close()

			except IOError:
				print ("Cannot get Message History")			

		elif choice == 4:
			try:
				os.remove("Message History.csv")
			except OSError:
				print ("Cannot delete file.")
			
		elif choice == 5:
			temp = os.system("clear")
			AddressBook.display()

		elif choice == 6: #CHANGE FILE AS WELL
			temp = os.system("clear")
			add_again = True
			
			while add_again is True:
				count = AddressBook.count()
				if (count < 300):	
					add_person = raw_input("Enter Name: ")
					host = raw_input("Enter Host: ")
					port = raw_input("Enter Port: ")

					AddressBook.add(add_person,host,int(port))
					add_again = GoAgain(choice)
			else:
				print ("Too many contacts! Please delete some!")
				add_again = False
			
		elif choice == 7: #CHANGE FILE AS WELL
			temp = os.system("clear")
			delete_again = True
		
			while delete_again is True:
				count = AddressBook.count()
				if (count > 12):
					delete_person = raw_input("Enter Name: ")
					AddressBook.delete(delete_person)	
					delete_again = GoAgain(choice)
				else:
					print ("Can't delete any more contacts!")
					delete_again = False

		elif choice == 8:
			temp = os.system("clear")
			print ("Program Terminated!")
			break

		else:
			print("Invalid Input! Please enter a choice from 1-6")

	SaveMessageHistory()	
	sys.exit(0)
	
def main():
	
	StartServer = threading.Thread(target = Server)
	StartServer.daemon = True
	StartServer.start()

	Menu()

	StartServer.join()

main()

