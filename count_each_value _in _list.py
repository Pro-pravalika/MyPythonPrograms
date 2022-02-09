def sample(value):
    print({each:value.count(each)for each in value})
sample([2,2,3,1,5,6,5,6,6,8,9,7,7,7,0,0,0])