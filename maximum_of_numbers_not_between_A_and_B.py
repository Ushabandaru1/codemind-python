n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in l:
    if i>=a and i<=b:
        pass
    else:
        s.append(i)
if len(s)==0:
    print("-1")
else:
    print(max(s))
        