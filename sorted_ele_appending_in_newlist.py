def sample(l):
    print(l.sort())
    count=1
    l3=[]
    for each in l:
        count=each-1
        l3.append(count)
        print(l3)
    
sample([5,6,9,3,90,87,65])
