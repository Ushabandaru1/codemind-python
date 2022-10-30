n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
for i in l:
    if i>=a and i<=b:
        pass
    else:
        d.append(i)
if len(d)==0:
    print("-1")
else:
    print(*d)