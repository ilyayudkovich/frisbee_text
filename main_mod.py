#!/usr/bin/env python
import smtplib
import argparse
import os

from weather import getCurrentWTC
from email_mod import lastSendIsGood
from utilities import getLogin, carrierMap

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def goToDir():
    dir_path = os.path.dirname(os.path.realpath('main_mod.py'))
    os.chdir(dir_path)
    # do an assert here that we are in the right directory

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

def numInContacts(phone):
    return str(phone) in open('./docs/contacts').read()

def getContact(phone):
    with open('./docs/contacts', 'r') as f:
        for line in f:
            if phone in line:
                return line

def generateMsg(kind, time, loc, message=None):
    if not message:
        wind, temp, clouds = getCurrentWTC('02115')
        wind = "The wind speed is " + wind + "mph "
        temp = "The temperature will be " + temp + "F "
        clouds = "and " + clouds.lower()
        message = temp + wind + clouds
    msg = """From: Northeastern Ultimate\nSubject: %s tn @ %s, %s\n%s""" % (kind, time, loc, message)
    return msg

def sendOne(number, user, server, body):
    if numInContacts(number):
        logger.info("Sending message to %s", number)
        server.sendmail(user, getContact(number), body)


def sendAll(numbers, user, server, body):
    for n in numbers:
        sendOne(n, user, server, body)

def main():
    goToDir()
    logging.info("About to connect to server")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    user, pw = getLogin()
    server.login(user, pw)

    parser = argparse.ArgumentParser(description='Send practice texts to NEU Ultimate')
    parser.add_argument('-c', help='Send cancelled message', action='store_true', default=False, dest='cancelled')
    parser.add_argument('-s', help='Send single text', action='store_true', default=False, dest='single')
    parser.add_argument('kind', action='store')
    parser.add_argument('time', action='store')
    parser.add_argument('location', action='store')
    results = parser.parse_args()

    if results.cancelled:
        logger.info("Preparing cancelled message")
        body = generateMsg(results.kind, results.time, results.location, message='CANCELLED')
    else:
        logger.info("Preparing regular message")
        body = generateMsg(results.kind, results.time, results.location)
    if results.single:
        logger.info("Sending singular message")
        number = input('Enter phone number: ')
        contact = getContact(str(number))
        if not contact:
            carrier = input('Enter the carrier: ')
            carrier = carrierMap[carrier]
            contact = str(number) + '@' + carrier
        sendOne(contact, user, server, body)
    else:
        logger.info("Sending mass message")
        sendAll(getNumbers(), user, server, body)
    server.quit()


if __name__ == '__main__':
    main()
