a=int(input())
e=[]
for i in range(a):
    d=0
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    for l in c:
        d=(d+1 if l<=0 else d )
    #print (d,b[1])
    if d<b[1]:
        e.append('YES')
    else:
        e.append('NO')
for i in e:
    print (i)
    
