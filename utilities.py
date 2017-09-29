carrierList = ['txt.att.net',
		'tmomail.net',
		'vtext.com',
		'messaging.sprintpcs.com',
		'myboostmobile.com',
		'comcastpcs.textmsg.com',
		'sms.edgewireless.com',
		'mymetropcs.com',
		'vmobl.com']

carrierMap = {'att':'txt.att.net',
		'tmobile':'tmomail.net',
		'verizon':'vtext.com',
		'sprint':'messaging.sprintpcs.com',
		'boost':'myboostmobile.com',
		'comcast':'comcastpcs.textmsg.com',
		'edge':'sms.edgewireless.com',
		'metro':'mymetropcs.com',
		'virgin':'vmobl.com'}

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

