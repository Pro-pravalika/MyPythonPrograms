from functools import reduce
numbers = [23,67,40,79,18,37,24,18]
sum = reduce(lambda x ,y:x+y , numbers)
print(sum)