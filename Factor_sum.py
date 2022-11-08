def r(n):
    c=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0 and i!=n//i:
            c+=i+n//i
        elif n%i==0 and i==n//i:
            c+=i
    return str(c)
l=input()
l=l.split(",")
k=[]
for i in l:
    if r(int(i)) in l:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    k.sort()
    print(*k)