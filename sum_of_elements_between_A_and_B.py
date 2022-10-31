n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in l:
    if i>=a and i<=b:
        c.append(i)
if len(c)!=0:
    print(sum(c))
else:
    print("-1")