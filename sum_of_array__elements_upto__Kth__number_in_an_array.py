n=int(input())
l=list(map(int,input().split()))
m=int(input())
y=[]
c=0
for i in l:
    if i not in y:
        y.append(i)
    if i==m:
        break
for j in y:
    c+=j
print(c)
    