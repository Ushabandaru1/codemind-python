n=int(input())
l=list(map(int,input().split()))
s=[]
t=[]
for k in l:
    if k not in s:
        s.append(k)
for i in s:
    if l.count(i)==i:
        t.append(i)
if len(t):
    print(t[0],t[-1])
else:
    print("-1")
