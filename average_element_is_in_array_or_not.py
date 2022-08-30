n=int(input())
l=list(map(int,input().split()))
sl=sum(l)
avg=sl//n
if avg in l:
    print("True")
else:
    print("False")