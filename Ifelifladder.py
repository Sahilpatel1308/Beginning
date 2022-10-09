#Given a variable D (distance) write a program to print the cost associated with it as shown in the image:-
a = int(input("Write the total distance covered "))
p = ("The total amount is ")
if a <= 100:
    print ( p + "5")
elif a <= 500:
    print ( p + "8")
elif a<= 1000:
    print ( p + "10")
else:
    print ( p + "12")