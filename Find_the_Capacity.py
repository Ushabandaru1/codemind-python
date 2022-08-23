s,t,b=map(int,input().split())
byts=2*s*t*b*512
capacty=byts//1024
print(capacty,end='KB')