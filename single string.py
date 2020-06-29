def chars(a, b):
  newa = b[:2] + a[2:]
  newb = a[:2] + b[2:]
  return newa + ' ' + newb
a=input("enter the a string:")
b=input("enter the b string:")
print(chars(a,b))