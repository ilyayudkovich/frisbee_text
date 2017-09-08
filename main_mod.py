#!/usr/bin/env python
import os
import sys
import smtplib
import pywapi
import time
import reader
from weather import getCurrentWTC
from email_mod import lastSendIsGood
from utilities import getLogin, carrierMap

<<<<<<< Updated upstream
def getNumbers():
    numbers = []
    with open('./docs/numbers', 'r') as f:
        for x in f:
            x = x.rstrip()
            if x:
                numbers.append(x)
    f.close()
    return numbers
=======
# def getNumbers():
# 	numbers = []
# 	with open('./docs/numbers', 'r') as f:
# 		for x in f:
# 			x = x.rstrip()
# 			if x:
# 				numbers.append(x)
# 	f.close()
# 	return numbers
>>>>>>> Stashed changes

def writeToContacts(phone, carrierMap):
    with open('./docs/contacts', 'a+') as f:
        contact = phone + '@' + carrierMap + '\n'
        print 'Adding contact ', contact, 'to contacts file'
        f.write(contact)
    f.close()

<<<<<<< Updated upstream
def writeToContacts(numbers):
    with open('./docs/contacts', 'a+') as f:
        for num in numbers:
            if not numInContacts(num):
                f.write(num + '\n')
    f.close()
=======
# def writeToContacts(numbers):
# 	with open('./docs/contacts', 'a+') as f:
# 		for num in numbers:
# 			if not numInContacts(num):
# 				f.write(num + '\n')
# 	f.close()
>>>>>>> Stashed changes

def numInContacts(phone):
    return phone in open('./docs/contacts').read()

def getContact(phone):
    with open('./docs/contacts', 'r') as f:
        for line in f:
            if phone in line:
                return line

def generateMsg():
    wind, temp, clouds = getCurrentWTC('02115')
    wind = "The wind speed is " + wind + "Mph. "
    temp = "The temperature will be " + temp + "F.\n"
    clouds = "The sky will be: " + clouds
    message = temp + wind + clouds
    msg = """From: Northeastern Ultimate\nSubject: Practice tn @ 7\n%s""" % message

    return msg

def sendOne(number, user, server, body):
    if numInContacts(number):
        print 'have correct contact infor for', number
        server.sendmail(user, getContact(number), body)
        print 'message sent'
    else:
        i = 0
        server.sendmail(user, number + '@' + carrierMap[i], body)
        time.sleep(5)
        i += 1
        while not lastSendIsGood() and i < len(carrierMap):
            server.sendmail(user, number + '@' + carrierMap[i], body)
            time.sleep(5)
            i += 1
        writeToContacts(number, carrierMap[i - 1])

def sendAll(numbers, user, server, body):
    for n in numbers:
        sendOne(n, user, server, body)

def main():
    user, pw = getLogin()
    server.login(user, pw)
    body = generateMsg()
    if reader.practiceToday(reader.dates):
        print "There is practice today"
    else:
        print "No practice today"
    # Testing space currently
    # server.sendmail(user,'yudkovich.i@husky.neu.edu', body)
    # sendAll(numbers, user, server, body)
    server.quit()


if __name__ == '__main__':
    main()
