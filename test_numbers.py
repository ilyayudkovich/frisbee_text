#!/usr/bin/env python
import os
import sys
import smtplib
import pywapi
from weather import getCurrentConditions
from email import lastSendIsGood

def getLogin():
	with open('./login', 'r') as f:
		email = f.readline()
		pw    = f.readline()
		return (email, pw)

def generateMsg():
	result = getCurrentConditions('02115')
	wind_s = result['wind']['speed'] + 'mph\n'
	wind_s = "The wind speed is " + wind_s
	temp = result['temperature'] + 'C\n'
	temp = "The temperature will be " + temp
	message = "Reminder you have practice tonight\n"
	message = message + temp + wind_s
	msg = """From: Northeastern Ultimate\nSubject: Practice\n%s""" % message

	print msg
	return msg

def main():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	numbers = []
	nem = {'att':'txt.att.net',
			'tmobile':'tmomail.net',
			'verizon':'vtext.com',
			'sprint':'messaging.sprintpcs.com'}
	with open('./numbers', 'r') as f:
		for x in f:
			x = x.rstrip()
			if x:
				numbers.append(x)
	user, pw = getLogin()
	server.login(user, pw)

	body = generateMsg()
	print body
	server.sendmail(user, '@txt.att.net' , body)
	if not lastSendIsGood():
		# Shove logic to try another carrier here
		pass

	print "message sent"
	server.quit()






if __name__ == '__main__':
    main()
