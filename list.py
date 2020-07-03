def read(a):
        with open(a) as file:     
                list = file.readlines()
                print(list)
a=input("enter the file name:")
read(a)