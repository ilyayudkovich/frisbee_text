#!/usr/bin/env python
import os
import sys
import smtplib
import pywapi
import time
import argparse

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

def getContacts():
    contacts = []
    with open('./docs/contacts', 'r') as f:
        for con in f:
            con = con.rstrip()
            if con:
                contacts.append(con)
    f.close()
    return contacts

def writeToContacts(phone, carrierMap):
    with open('./docs/contacts', 'a+') as f:
        contact = phone + '@' + carrierMap + '\n'
        print 'Adding contact ', contact, 'to contacts file'
        f.write(contact)
    f.close()

def writeToContacts(numbers):
    with open('./docs/contacts', 'a+') as f:
        for num in numbers:
            if not numInContacts(num):
                f.write(num + '\n')
    f.close()

def numInContacts(phone):
    return phone in open('./docs/contacts').read()

def getContact(phone):
    with open('./docs/contacts', 'r') as f:
        for line in f:
            if phone in line:
                return line

def generateMsg(time, loc):
    wind, temp, clouds = getCurrentWTC('02115')
    wind = "The wind speed is " + wind + "mph "
    temp = "The temperature will be " + temp + "F "
    clouds = "and " + clouds.lower()
    message = temp + wind + clouds
    msg = """From: Northeastern Ultimate\nSubject: Practice tn @ %s, %s\n%s""" % (time, loc, message)

    return msg

def generareCancelMsg(time, loc):
    msg = """From: Northeastern Ultimate\nSubject: Practice tn @ %s, %s\n%s""" % (time, loc, "CANCELLED")
    return msg

def sendOne(number, user, server, body):
    if numInContacts(number):
        print 'have correct contact infor for', number
        server.sendmail(user, getContact(number), body)

def sendAll(numbers, user, server, body):
    for n in numbers:
        sendOne(n, user, server, body)

def main():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    user, pw = getLogin()
    server.login(user, pw)
    parser = argparse.ArgumentParser(description='Send practice texts to NEU Ultimate')
    parser.add_argument('-c', action='store_true', default=False, dest='cancelled')
    parser.add_argument('time', action='store')
    parser.add_argument('location', action='store')
    results = parser.parse_args()
    if results.cancelled:
        print "generating cancelled message"
        body = generareCancelMsg(results.time, results.location)
    else:
        print "generating regular message"
        body = generateMsg(results.time, results.location)
    sendAll(getNumbers(), user, server, body)
    server.quit()


if __name__ == '__main__':
    main()
