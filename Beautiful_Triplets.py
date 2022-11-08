n=int(input())
l=list(map(int,input().split()))
l.sort()
d=[]
for i in l:
    if i not in d:
        d.append(i)
c=0
k=1
for i in d:
    for j in range(k,len(d)):
        d[j]-=i
    k+=1
for i in range(len(d)):
    c=0
    for j in range(len(l)):
        l[j]=l[j]-d[i]
        if l[j]>=0:
            c+=1
    print(c)
        