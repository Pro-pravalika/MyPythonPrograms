def num(ele):
	p=list(filter(lambda x:(x<0),ele))
	for i in ele:
		if i%2==0:
			if i>=1:
				print(i)
num([20,16,78,-34,67,-6,5])