def sample(value):
    for i in value:
        if i==2:
            return(value.count(i))
print(sample([12,34,2,87,2,95,20,2]))