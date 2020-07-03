def unique(list1): 
    uniquelist =[] 
    for x in list1: 
        if x not in uniquelist: 
            uniquelist.append(x) 
    for x in uniquelist: 
        print(x)
list1 = [10, 20, 10, 30, 40, 40] 
print("the unique values from 1st list is") 
unique(list1)