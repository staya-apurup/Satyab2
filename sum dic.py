def sum(d2):
    sum=0
    for i in d2:
        sum=sum+d2[i]
    return sum
d2={"a":12,"b":8,"c":15}
print("sum of items in the dictionary:",sum(d2))