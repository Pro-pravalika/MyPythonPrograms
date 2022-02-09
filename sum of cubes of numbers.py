def sample(n):
	s=0
	for i in range(1,n+1):
		s=s+(i*i*i)
	return s 
print(sample(10))