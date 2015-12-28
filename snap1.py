a=input().split()
a=[int(i) for i in a]
b=input().split()
b=[int(i) for i in b]
z=[]
for i in range(a[1]):
    d=input().split()
    d=[ int(i) for i in d]
    if not d[2]:
        if d[0] in b:
            ind = b.index(d[0])+d[1]
            z.append(b[ind]  if ind <= len(b)-1 else -1 )
        else:
            if d[0] < max(b):
                m=min([i for i in b if i>d[0]])
                ind1=b.index(min([i for i in b if i>d[0]]))+d[1]-1
                z.append(b[ind1] if ind1<= len(b)-1 else -1)
            else:
                z.append(-1)
    else:
        if d[0] in b:
            ind=b.index(d[0])-d[1]
            z.append(b[ind] if ind>=0 else -1 )
        else:
            if d[0] > min(b):
                m=max([i for i in b if i<d[0]])
                ind1=b.index(max([i for i in b if i<d[0]]))-d[1]+1
                z.append(b[ind1] if ind1>=0 else -1)
            else:
                z.append(-1)
for i in z:
    print(i)
        
