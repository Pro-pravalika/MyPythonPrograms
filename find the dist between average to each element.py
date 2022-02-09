total=0
list=[1,2,45,36,75,49,25,50,37,20,23]
for ele in range(2,len(list)):
	total=total+list[ele]
avg=total/len(list)
print(avg)
for each in list:
	dist=each-avg
	print(dist)