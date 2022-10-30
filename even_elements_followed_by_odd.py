n=int(input())
l=list(map(int,input().split()))
el=[]
ol=[]
for i in l:
    if i%2==0:
        el.append(i)
    else:
        ol.append(i)
print(*(el+ol))