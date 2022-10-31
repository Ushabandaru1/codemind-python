n=int(input())
l=list(map(int,input().split()))
y=[]
c=0
for i in l:
    if i%2!=0:
        y.append(i)
    if i%2==0:
        break
for j in y:
    c+=j
print(c)
    