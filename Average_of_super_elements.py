n=int(input())
l=list(map(int,input().split()))
s=0
c=0
y=[]
for k in l:
    if k not in y:
        y.append(k)
for i in y:
    if l.count(i)==i:
        s+=i
        c+=1
if c!=0:
    avg=s/c
    print(format(avg,'.2f'))
else:
    print("-1")