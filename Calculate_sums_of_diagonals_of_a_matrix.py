n=int(input().strip())
a=[[0]*n for i in range(n)]
for j in range(n):
    a[j]=[int(k) for k in input().strip().split(" ")]
x=0
y=0
for j in range(n):
    for k in range(n):
        if j==k:
            x=x+a[j][k]
for j in range(n):
    for k in range(n):
        if (n-j-1)==k:
            y=y+a[j][k]
print("Principal Diagonal:%d"%x)
print("Secondary Diagonal:%d"%y)