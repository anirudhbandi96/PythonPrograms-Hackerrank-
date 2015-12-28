a=int(input())
c=[]
sum1=sum2=0
for i in range(a):
    b=list(map(int,input().split()))
    c.append(b)
for i in range(a):
    for j in range(a):
        if (i+j==(a-1)):
            sum1=sum1+c[i][j]
        if (i==j):
            sum2=sum2+c[i][j]
print(abs(sum2-sum1))
    
