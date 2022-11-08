n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s1=s2=0
for i in l1:
    s1+=i
for i in l2:
    s2+=i
if s1>s2:
    print(0)
else:
    print(s2-s1)