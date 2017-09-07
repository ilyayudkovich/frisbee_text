#!/usr/bin/env python

import imaplib
import time
import email
from utilities import getLogin

INBOX  = 'Inbox'
FAILED = 'Failed'

def printMailBoxes():
	user, pw = getLogin()
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(user, pw)
	rv, mailboxes = mail.list()
	print mailboxes

# This will fail if it's not Inbox or Failed at the moment
# Definitely needs some formatting
def getBox(box):
	if box.lower() not in [INBOX.lower(), FAILED.lower()]:
		print "Defaulting to inbox"
		box = INBOX
	user, pw = getLogin()
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(user, pw)
	mail.select(box)
	return mail

def getInbox():
	return getBox('Inbox')

def getFailedBox():
	return getBox('Failed')

def getFailedMessages():
	failedBox = getFailedBox()
	latest_email = getLastestEmail(failedBox)
	print latest_email


def deleteEmail(mailbox, mid):
	mailbox.store(mid, '+FLAGS', '\\Deleted')
	mailbox.expunge()
	print 'Message', mid, 'has been deleted'

def getSender(raw_string):
	email_bod = email.message_from_string(raw_string)
	return email_bod['From']

def getSubject(raw_string):
	email_bod = email.message_from_string(raw_string)
	return email_bod['Subject']

# TODO (IY): clean this up, seems like you should check for an empty mailbox
def getLastestEmail(mailbox):
	typ, data = mailbox.search(None, 'ALL')
	loe = data[0].split()
	# if the mailbox isn't empty
	if len(loe) > 0:
		typ, data = mailbox.fetch(loe[-1], '(RFC822)')
		msg = data[0][1]
		raw_string = msg.decode('utf-8')
		if checkBadEmail(raw_string):
			print 'Email was bad, deleting'
			deleteEmail(mailbox, loe[-1])
			return (None, None)
		else:
			print 'Email is good, returning it'
			return (msg, loe[-1])
	else:
		print 'Email is good, returning it'
		return ("good", 1)

def lastSendIsGood():
	print "checking last send is good"
	failedBox = getFailedBox()
	msg, em_id = getLastestEmail(failedBox)
	if msg:
		return True
	else:
		return False

def checkBadEmail(raw_string):
	badSender = 'Mail Delivery Subsystem <mailer-daemon@googlemail.com>'
	# badSubject = 'Delivery Status Notification (Failure)'
	subject = getSubject(raw_string)
	sender = getSender(raw_string)
	return sender == badSender
