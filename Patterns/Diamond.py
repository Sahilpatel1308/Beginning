for i in range (0,4):
    if i==0:
        print(" "*(4), end="")
        print("*")
    else:
        print(" "*(4-i), end="")
        print("*", end="")
        print(" "*((i*2)-1), end="")
        print("*")