a=list(map(int,input().split()))
m=[]
z=[]
for i in range(a[0]):
    m.append(list(map(int,input().split())))
#print(m)
n=min(a[0],a[1])
for i in range(int(n/2)):
    b=[]
    for j in range(a[0]):
        for k in range(a[1]):
            print(j,k)
            if (j==i and k in range(i,a[1]-i))or(j==a[0]-i-1 and k in range(i,a[1]-i))or(k==i and j in range(i,a[0]-i) )or(k==a[1]-i-1 and j in range(i,a[0]-i)):
                print('entered loop',i,j,k)
                b.append(m[j][k])
    z.append(b)

