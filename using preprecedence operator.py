def sample(a,s,p):
	if(a>0):
		return a**p>5 and s-a//p>20 or s**2==5
print(sample(10,3,5))