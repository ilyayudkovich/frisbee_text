carrierMap = ['txt.att.net',
		'tmomail.net',
		'vtext.com',
		'messaging.sprintpcs.com',
		'myboostmobile.com',
		'comcastpcs.textmsg.com',
		'sms.edgewireless.com',
		'mymetropcs.com',
		'vmobl.com']

def getLogin():
	with open('./docs/login', 'r') as f:
		email = f.readline()
		pw    = f.readline()
		return (email, pw)

def formatPhoneNumber(phone):
	pass

def parseMessage():
	pass

def failSend():
	pass

