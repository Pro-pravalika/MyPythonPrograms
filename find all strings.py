import re 
names = 'Pandu,Sony,Nikki,Nikhil'

result = re.findall(r'[A-Z][a-z]+',names)
print(result)

import re 
sample = 'python,Pandas,Django,HTML,143,java'
result = re.findall(r'[A-Z]+',sample)
print(result)