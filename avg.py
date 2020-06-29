print("Input some integers to calculate their average. ")
count = 0
sum = 0
for i in range(0,10):
    number = int(input(""))
    sum = sum + number
    count += 1
if count == 0:
    print("Input some numbers")
else:
    print("Average of the above numbers are: ", sum / (count))