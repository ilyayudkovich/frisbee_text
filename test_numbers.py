#!/usr/bin/env python
import os
import sys
import smtplib
import pywapi
import time
from weather import getCurrentConditions
from email_utils import lastSendIsGood
from utilities import getLogin

def getNumbers():
	numbers = []
	with open('./docs/numbers', 'r') as f:
		for x in f:
			x = x.rstrip()
			if x:
				numbers.append(x)
	f.close()
	return numbers

def writeToContacts(phone, carrier):
	with open('./docs/contacts', 'a+') as f:
		contact = phone + '@' + carrier + '\n'
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
	result = getCurrentConditions('02115')
	wind_s = result['wind']['speed'] + 'mph\n'
	wind_s = "The wind speed is " + wind_s
	temp = result['temperature'] + 'C\n'
	temp = "The temperature will be " + temp
	message = "Reminder you have practice tonight\n"
	message = message + temp + wind_s
	msg = """From: Northeastern Ultimate\nSubject: Practice\n%s""" % message

	return msg

def main():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	nem = ['txt.att.net',
			'tmomail.net',
			'vtext.com',
			'messaging.sprintpcs.com']

	numbers = getNumbers()
	user, pw = getLogin()
	server.login(user, pw)
	body = generateMsg()
	for n in numbers:
		if numInContacts(n):
			print 'have correct contact info'
			server.sendmail(user, getContact(n), body)
			print 'message sent'
		else:
			i = 0
			server.sendmail(user, n + '@' + nem[i], body)
			time.sleep(5)
			while not lastSendIsGood() and i < len(nem):
				server.sendmail(user,n + '@' + nem[i], body)
				time.sleep(5)
				i += 1
			writeToContacts(n, nem[i])
	server.quit()


if __name__ == '__main__':
    main()
