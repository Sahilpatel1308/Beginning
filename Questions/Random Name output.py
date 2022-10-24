#Type a program that shows up the random name of friends that went for a party to pay the bill.

import random
n = input("Type the names of all the friends separated by , ")
l = n.split(",")
c = len(l)
p = random.randint(0, c-1)
r = l[p]
print (f"The bill will be paid by {r}.")