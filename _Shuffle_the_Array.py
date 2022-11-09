a=int(input())
l=list(map(int,input().split()))
mid=a//2
for i in range(mid):
    print(l[i],l[mid+i],end=" ")