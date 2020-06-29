def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]
s=input("enter the string:")
print("the original string is:")
print(s)
print("the  reverse string is:")
print(reverse(s))