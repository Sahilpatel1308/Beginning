n=int(input())
a = 4
for i in range(1,6):
    print("*"*i,end="")
    print(" "*a,end='')
    print("*"*i)
    a-=1