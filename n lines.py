def readfirst(a, n):
        from itertools import islice
        with open(a) as f:
                for l in islice(f,n):
                        print(l,end ='')
a=input("enter the file name:")
readfirst(a,2)