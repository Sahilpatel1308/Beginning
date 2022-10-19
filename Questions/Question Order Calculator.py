#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

#Based on a user's order, work out their final bill.

#Small Pizza: $15 Medium Pizza: $20 Large Pizza: $25 Pepperoni for Small Pizza: +$2 Pepperoni for Medium or Large Pizza: +$3

#Extra cheese for any size pizza: + $1print("Welcome to Python Pizza Deliveries!")
a = input("What size pizza do you want? S, M, or L? ")
b = input("Do you want pepperoni? Y or N? ")
c = input("Do you want extra cheese? Y or N? ")
if a=="S":
    d = int(15)
    if b=="Y":
        e=int(2)
    else:
        e=0
elif a=="M":
    d=int(20)
    if b=="Y":
        e=int(3)
    else:
        e=0
else:
    d=int(25)
    if b=="Y":
        e=int(2)
    else:
        e=0
if c=="Y":
    f=int(1)
else:
    f=0

g = int (d+e+f)
k = str(g)
print("Your final bill is: $" + k + ".")


