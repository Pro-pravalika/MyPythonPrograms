import re
string = "Date of birth 29 year 2000 week 4 th.."
pattern = ' \d+ '
result = re.findall(pattern,string)
print(result)


import re 
names = 'Pandu,Sony,Nikki,Nikhil'

result = re.findall(r'[A-Z][a-z]+',names)
print(result)

import re 
sample = 'python,Pandas,Django,HTML,143,java'
result = re.findall(r'[A-Z]+',sample)
print(result)