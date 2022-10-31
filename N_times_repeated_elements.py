n=int(input())
l=list(map(int,input().split()))
k=int(input())
y=[]
n=[]
for i in l:
    if i not in y:
        y.append(i)
for j in y:
    if l.count(j)==k:
        n.append(j)
if len(n)==0:
    print("-1")
else:
    print(*n)
        