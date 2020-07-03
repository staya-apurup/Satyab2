def read(a):
        from itertools import islice
        with open(a,"w") as file:
                file.write("Python Exercises\n")
                file.write("Java Exercises")
        txt = open(a)
        print(txt.read())
read('gitam.txt')