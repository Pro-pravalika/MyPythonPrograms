test_str = "GeeksForGeeks"
print(test_str)
print(len(test_str))
new_str = " "
for i in range(len(test_str)):
	if i !=5:
		new_str = new_str+test_str[i]
print(new_str)
