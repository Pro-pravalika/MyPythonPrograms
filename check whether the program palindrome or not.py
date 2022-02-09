def poly(char):
	if char==char[::-1]:
		return char
	else:
		return 'it is not a polyndrome'
print(poly('malayalam'))