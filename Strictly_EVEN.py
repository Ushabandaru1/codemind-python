n=int(input())
l=list(map(int,input().split()))
d=0
e=0
for i in range(0,n):
    if i%2==0 and l[i]%2==0:
        d+=1
    if l[i]%2==0:
        e+=1
if d==e:
    print("True")
else:
    print("False")