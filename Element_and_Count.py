n=int(input())
l=list(map(int,input().split()))
y=[]
c=0
for i in l:
    if i not in y:
        y.append(i)
for j in y:
    c=l.count(j)
    print(j,c,end=' ')
    