l= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l= [x for (i,x) in enumerate(l) if i not in (0,4,5)]
print(l)