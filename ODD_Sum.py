n=int(input())
l=list(map(int,input().split()))
es=0
for i in range(n):
    if l[i]%2!=0:
        es=es+l[i]
print(es)