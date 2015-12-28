import math
z=[]
a="".join(input().split())
length=len(a)
r=math.floor(pow(length,0.5))
c=math.ceil(pow(length,0.5))
splits=[ a[x:x+c] for x in range(0,length,c)]
for j in range(c):
    for i in splits:
        if(j<len(i)):
            z.append(i[j])
        else:
            continue
    if j!=(c-1):
        z.append(" ")
print( "".join(z))
    

