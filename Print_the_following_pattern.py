a=int(input())
l=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(a):
    for j in range(a-(i+1)):
        print(" ",end="")
    for j in range(i+1):
        print(l[j],end="")
    for j in range(i-1,-1,-1):
        print(l[j],end="")
    print()