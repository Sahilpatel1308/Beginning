
for j in range (6,0,-1):
  if j>3:
    print("*", end="")
    print(" "*(j-3), end="")
    print("*", end="")
    print()
  elif j==3 or j==2:
    print("*"*(j-(j-1)), end="")
for i in range (0,6):
  if i<=2:
    print("*"*i)
  elif i>2 or i<5:
    print("*", end="")
    print(" "*(i-2), end="")
    print("*", end="")
    print()

