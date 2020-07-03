l=[("x",1),("y",2),("z",3)]
d={}
for a,b in l:
    d.setdefault(a, []).append(b)
print(d)