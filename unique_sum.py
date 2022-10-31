n=int(input())
l=list(map(int,input().split()))
y=set(l)
c=0
for i in y:
    c+=i
print(c)