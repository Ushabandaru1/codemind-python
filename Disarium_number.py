n=int(input())
t=n
s=0
y=0
while n:
    y=(y*10)+n%10
    n=n//10
    i=1
while y:
    s+=(y%10)**i
    y=y//10
    i+=1
if s==t:
    print(True)
else:
    print(False)