'''
Copyright (c) 2015 Manpreet Bahl

This file contains variables and a 
function that is shared between 
multiple files.
'''

#Variables
username = "manpreet20"
version = "0.2"
key = ""
rounds = 20
buf = 1024

global messages
messages = []

#Display the Message array
def display():
	print "\n\n".join(messages)
