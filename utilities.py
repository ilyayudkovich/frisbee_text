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

