def func(a,d):
    print('function called')
    a.append(d)
    print(a)
f=[0]
a=list(map(int,input().split()))
print(a)
b=[]
for i in range(a[0]):
    b.append(list(map(int,input().split())))
for i in range(int(min(a[0],a[1])/2)):
    c=[]
    for j in range(a[0]):
        d=[]
        f=[0,1,2,3]
        for k in range(a[1]):
            print('i,j,k',i,j,k)
            if(j==i and k in range(i,a[1]-i)):
                print('entered 1')
                print(c)
                c.append(b[j][k])
            elif(k==a[1]-i-1 and j in range(i+1,a[0])):
                print('entered 2')
                c.append(b[j][k])
                print(c)
            elif(j==a[0]-i-1 and k in range(i,a[1]-i-1)):
                print('entered 3')
                d.append(b[j][k])
            elif(k==i and j in range(i+1,a[0]-i-1)):
                print('entered 4')
                print(b[j][k])
                func(f,2)
            else:
                continue
    d.reverse()
    print('d',d)
    print('f',f)
    f.reverse()
    for m in d:
        c.append(m)
    for m in f:
        c.append(m)
    print(c)
     
                
                
