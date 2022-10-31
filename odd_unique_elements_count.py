n=int(input())
l=list(map(int,input().split()))
c=0
y=[]
for i in l:
    if i not in y:
        y.append(i)
for j in y:
    if j%2!=0:
        c+=1
print(c)
        