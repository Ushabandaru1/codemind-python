n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
a=set(x)
b=set(y)
d=[]
o=[]
for k in a:
    if k not in b:
        o.append(k)
for h in b:
    if h not in a:
        o.append(h)
for i in a:
    d.append(i)
for j in b:
    d.append(j)
v=set(d)
print(len(v)-len(o))

    