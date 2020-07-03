with open("abc.txt")as f:
    with open("out.txt","w")as f1:
        for line in f:
            f1.write(line)
11.python program to sum all the items in the list.
total=0
list=[1,5,7,9,8,20]
for i in range(0,len(list)):
    total=total+list[i]
print("sum of all elements in the list:",total)