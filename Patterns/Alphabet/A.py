for i in range (0,5):
    if i==0:
        print(" "*(6), end="")
        print("*")
    elif i==2:
        print ("   *******")
    elif i<=5:
        print(" "*(5-i), end="")
        print("*",end="")
        print(" "*((2*i)+1), end="")
        print("*")
    
    

# for i in range (6,0,-1):
#     for j in range (0, i-1):
#         print("* ", end="")
#     print("")