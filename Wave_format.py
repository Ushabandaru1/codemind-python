a=int(input())
l=list(map(int,input().split()))
l.sort()
if a%2!=0:
    for i in range(a-1,1,-2):
        if i==2:
            print(l[i-1],end=" ")
            print(l[i],end=" ")
        else:
            print(l[i-1],end=" ")
            print(l[i],end=" ")
    print(l[0])
else:
    for i in range(a-1,0,-2):
        print(l[i-1],end=" ")
        print(l[i],end=" ")