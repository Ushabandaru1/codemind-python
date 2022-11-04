s1=input()
s2=input()
c=[]
s1=s1.lower()
s2=s2.lower()
a=s1.split()
b=s2.split()
for i in b:
    if i in a:
        c.append(i)
print(*c)

        