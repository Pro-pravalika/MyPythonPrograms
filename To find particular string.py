import re 
def sample(text):
	string = 'abc'
	if re.search(string, text):
		print(string)
	else:
		print("not matched")
sample("b")
sample("abc")
