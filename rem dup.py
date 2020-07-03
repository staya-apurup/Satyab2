from itertools import groupby
x = [2,3,4,5,5,5,6,7,7,8,9]
print([i[0] for i in groupby(x)])