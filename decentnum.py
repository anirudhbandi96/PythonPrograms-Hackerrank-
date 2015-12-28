z=[]
for i in range(int(input())):
    s={}
    n=int(input())
    for i in range(n):
        for j in range(n):
            if((5*i)+(3*j)==n):
                s[j]=i
    if not s:
        z.append(-1)
    else:
        z.append(int("5"*(3*max(s))+"3"*(5*s[max(s)])))
for i in z:
    print (i)
        
                
        
