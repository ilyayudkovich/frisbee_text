#!/usr/bin/env python
import os
import sys
import smtplib
import pywapi
import time
from weather import getCurrentWTC
from email_mod import lastSendIsGood
from utilities import getLogin, carrierMap

def getNumbers():
	numbers = []
	with open('./docs/numbers', 'r') as f:
		for x in f:
			x = x.rstrip()
			if x:
				numbers.append(x)
	f.close()
	return numbers

def writeToContacts(phone, carrierMap):
	with open('./docs/contacts', 'a+') as f:
		contact = phone + '@' + carrierMap + '\n'
		print 'Adding contact ', contact, 'to contacts file'
		f.write(contact)
	f.close()

def numInContacts(phone):
	return phone in open('./docs/contacts').read()

def getContact(phone):
	with open('./docs/contacts', 'r') as f:
		for line in f:
			if phone in line:
				return line

def generateMsg():
	wind, temp, clouds = getCurrentWTC('02115')
	wind = "The wind speed is " + wind + "Mph";
	temp = "The temperature will be " + temp + "F\n"
	clouds = "Heres what the sky looks like: " + clouds
	message = "Reminder you have practice tonight @ 7pm\n"
	message = message + temp + wind + clouds
	msg = """From: Northeastern Ultimate\nSubject: Practice\n%s""" % message

	return msg

# TODO (IY): You can probably turn this into sendOne and then expand into send many
def sendAll(numbers):
	for n in numbers:
	 	if numInContacts(n):
	 		print 'have correct contact info for', n
	 		server.sendmail(user, getContact(n), body)
	 		print 'message sent'
	 	else:
	 		i = 0
	 		server.sendmail(user, n + '@' + carrierMap[i], body)
	 		time.sleep(5)
	 		while not lastSendIsGood() and i < len(carrierMap):
	 			server.sendmail(user,n + '@' + carrierMap[i], body)
	 			time.sleep(5)
	 			i += 1
	 		writeToContacts(n, carrierMap[i])

def main():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	numbers = getNumbers()
	user, pw = getLogin()
	server.login(user, pw)
	body = generateMsg()
	# Testing space currently
	server.sendmail(user,'FAKE TARGET', body)
	time.sleep(5)
	print lastSendIsGood()
	server.quit()


if __name__ == '__main__':
    main()
