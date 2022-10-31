n=int(input())
l=list(map(int,input().split()))
y=[]
c=0
for i in l:
    if i not in y:
        y.append(i)
for k in y:
    if l.count(k)==k:
        c+=1
print(c)