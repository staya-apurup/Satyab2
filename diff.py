l1 = [2,5,6,8,3]
l2=[1,5,3,43,4]
diff1 = list(set(l1) - set(l2))
diff2= list(set(l2) - set(l1))
total = diff1 + diff2
print(total)