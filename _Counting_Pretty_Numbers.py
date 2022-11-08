t=int(input())
for i in range(0,t):
    c=0
    l,r=map(int,input().split())
    for i in range(l,r+1):
        r=i%10
        if r==2 or r==3 or r==9:
            c+=1
    print(c)
        