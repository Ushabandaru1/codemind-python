t=int(input())
while t:
    c=0
    n=int(input())
    l=list(map(int,input().split()))
    for i in l:
        if i%2!=0:
            c+=1
    if c%2!=0:
        c-=1
    print(c//2)