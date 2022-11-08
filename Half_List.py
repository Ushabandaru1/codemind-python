a=int(input())
l=list(map(int,input().split()))
b=a//2
a=l[::-1]
for i in range(b):
    print(a[i],end=" ")
for i in range(b):
    print(l[i],end=" ")