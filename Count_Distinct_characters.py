s=input()
s=s.replace(" ","")
s=s.lower()
l=[]
for i in s:
    l.append(i)
sl=[]
for i in l:
    if i not in sl:
        sl.append(i)
print(len(sl))