str = "pravalikapanduprava"
print(str)
new_str = ' '.join([str[i]for i in range(len(str)) if i != 6])
print(new_str)