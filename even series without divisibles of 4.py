n=int(input("Type value "))
for number in range (2, n+1):
    if number%2!=0:
                continue
    if number%4 == 0:
            continue
    print ( number )
    