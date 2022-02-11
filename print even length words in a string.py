def sample(string):
	string =string.split(' ')
	for word in string:
		if len(word)%2 == 0:
			return(word)
string = "pravalika"
print(sample(string))