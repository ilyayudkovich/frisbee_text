#!/usr/bin/env python
import os
import sys
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

def main():
	numbers = getNumbers()
	driver = carrierHomePage()
	contacts = getAllNumbers(driver, numbers)
	writeToContacts(contacts)

if __name__ == '__main__':
	main()
