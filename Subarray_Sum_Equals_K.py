n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(len(l)+1):
    for j in range(i):
        if sum(l[j:i])==k:
            c+=1
print(c)