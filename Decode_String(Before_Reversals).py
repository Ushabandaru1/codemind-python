t=int(input())
for i in range(0,t):
    a,b=map(int,input().split())
    s=input()
    while b>0:
        y=s[:b]
        y=y[::-1]
        s=y+s[b:]
        b-=1
    print(s)