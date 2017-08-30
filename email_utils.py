#!/usr/bin/env python

import imaplib
import time
import email
from utilities import getLogin

def getInbox():
	user, pw = getLogin()
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(user, pw)
	mail.select('inbox')
	return mail

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

def getLastestEmail(mailbox):
	typ, data = mailbox.search(None, 'ALL')
	loe = data[0].split()
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

def lastSendIsGood():
	inbox = getInbox()
	msg, mid = getLastestEmail(inbox)
	if msg:
		print 'Last email was good'
		return True
	else:
		print 'Try a different carrier'
		return False

def checkBadEmail(raw_string):
	badSender = 'Mail Delivery Subsystem <mailer-daemon@googlemail.com>'
	# badSubject = 'Delivery Status Notification (Failure)'
	subject = getSubject(raw_string)
	sender = getSender(raw_string)
	return sender == badSender

