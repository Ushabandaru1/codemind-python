def palind(n):
    x=str(n)
    y=x[::-1]
    if x==y:
        return True
    return False
n=int(input())
m=list(map(int,input().split()))
c=0
for i in m:
    if palind(i):
        c+=1
print(c)