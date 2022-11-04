s=input()
s=s.replace(" ","")
s=s.lower()
l=[]
for i in s:
    l.append(i)
sl=[]
for i in l:
    if l.count(i)==1:
        sl.append(i)
sl=sorted(sl)
for i in sl:
    print(i,end="")