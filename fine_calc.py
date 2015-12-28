a=list(map(int,input().split()))
b=list(map(int,input().split()))
print( 0 if a[2]<b[2] else 10000 if a[2]>b[2] else 500*(a[1]-b[1]) if a[1]>b[1] else 0 if a[1]<b[1] else
       15*(a[0]-b[0]) if a[0]>b[0] else 0)
            
