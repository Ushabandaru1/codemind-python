l=int(input())
r=int(input())
c=0
for i in range(l,r+1):
    su=0
    for j in range(i,r+1):
        su+=j
        if su%2!=0:
            c+=1
print(c)
    