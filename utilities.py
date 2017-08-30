def getLogin():
	with open('./login', 'r') as f:
		email = f.readline()
		pw    = f.readline()
		return (email, pw)

def parseMessage():
	pass

def failSend():
	pass

