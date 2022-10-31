n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,n):
    if l[i]%2==0:
        s.append(i)
if len(s)==len(l):
    print("True")
else:
    print("False")