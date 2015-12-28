l=int(input())
a=[]
for i in range(l):
    y=int(input())
    z=y
    while(z%3!=0):
        z-=5
    if(z<0):
        a.append('-1')
    else:
        a.append(z*'5'+(y-z)*'3' )
for i in a:
    print(i)
