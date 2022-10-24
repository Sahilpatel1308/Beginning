import random
n = input("Write the name of the cities you are confused to visit separated by comma ")
c = n.split(",")
o = random.choice(c)
print("You should visit " + o + " first.")