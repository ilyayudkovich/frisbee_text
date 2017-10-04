#!/usr/bin/env python
import os
import sys
import getpass
from webutils import carrierHomePage, getAllNumbers

# This should create the failed label in the gmail inbox and create a filter.
# probably use selenium to manually create the labels and set up the filters.
# Also setting up the contacts file should be done in here


def getNumbers():
	numbers = []
	with open('./docs/numbers', 'r') as f:
		for x in f:
			x = x.rstrip()
			if x:
				numbers.append(x)
	f.close()
	return numbers

def writeToContacts(contacts):
	with open('./docs/contacts', 'a+') as f:
		for c in contacts:
			if not numInContacts(c):
				f.write(c + '\n')
	f.close()

def writeToContacts(phone, carrierMap):
    with open('./docs/contacts', 'a+') as f:
        contact = phone + '@' + carrierMap + '\n'
        print 'Adding contact ', contact, 'to contacts file'
        f.write(contact)
    f.close()

# TODO: fix for RACE condition
def createDocsDir():
	if not os.path.exists('./docs'):
		os.makedirs('./docs')

def getServerLogin():
	email = raw_input('What is the email address that will be used: ')
	pw = getpass.getpass(prompt='What is the password for that email: ')
	print 'You entered email:', email, 'pw:', pw
	with open('./docs/login', 'a+') as f:
		f.write(email + '\n')
		f.write(pw + '\n')
	f.close()

# TODO: error checking
def addNumbers():
	numbers = []
	with open('./docs/numbers', 'a+') as f:
		while True:
			print "Make sure to only enter the 10  digits of the number"
			num = raw_input("Enter a number youd like to add (or Q to quit): ")
			if num == "Q":
				break
			else:
				numbers.append(num)
				f.write(num + '\n')
	f.close()
	return numbers

def main():
	createDocsDir()
	if not os.path.isfile('./docs/login'):
		getServerLogin()
	numbers = addNumbers()
	driver = carrierHomePage()
	contacts = getAllNumbers(driver, numbers)
	writeToContacts(contacts)

if __name__ == '__main__':
	main()
