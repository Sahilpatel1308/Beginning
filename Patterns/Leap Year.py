year = int (input("Which year do you want to check? "))
y = year
a = y%4
b = y%100
c = y%400
if (a==0):
    if (b!=0):
        print("Leap Year")
    elif (c==0):
        print("Leap Year")
else:
    print("Not Leap Year")
