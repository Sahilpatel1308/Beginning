n=int(input("PrintUntil "))
m=int(input("Stop at "))
for number in range (1, n+1):
    if number==int(m):
        break
    print ( number )