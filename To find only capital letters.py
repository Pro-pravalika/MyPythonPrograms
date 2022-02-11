import re 
sample = 'python,Pandas,Django,HTML,143,java'
result = re.findall(r'[A-Z]+',sample)
print(result)