import math
def func(i):
    print(i)
    if len(set(i))==1 or len(set(i))==0:
        return i
    a=list(i)
    for j in range(len(i)):
        if i[j]!=i[j+1]:
            if i[j:j+2]=="ab":
                a[j:j+2]="c"
                return func("".join(a))
            elif  i[j:j+2]=="ba":
                a[j:j+2]="c"
                return func("".join(a))
            elif i[j:j+2]=="cb":
                a[j:j+2]="a"
                return func("".join(a))
            elif i[j:j+2]=="bc":
                a[j:j+2]="a"
                return func("".join(a))
            elif i[j:j+2]=="ca":
                a[j:j+2]="b"
                return func("".join(a))
            elif i[j:j+2]=="ac":
                a[j:j+2]="b"
                return func("".join(a))
z=[]
for i in range(int(input())):
    z.append(input())
for i in z:
    c=len(func(func(i[:math.ceil(len(i)/2)])+func(i[math.ceil(len(i)/2):])))
    d=len(func(func(i[math.ceil(len(i)/2)-1::-1])+func(i[math.ceil(len(i)/2):])))
    e=len(func(func(i[math.ceil(len(i)/2)-1::-1])+func(i[len(i):math.ceil(len(i)/2)-1:-1])))
    f=len(func(func(i[:math.ceil(len(i)/2)])+func(i[len(i):math.ceil(len(i)/2)-1:-1])))
    a=len(func(i))
    b=len(func(i[len(i)::-1]))
    print(min(a,b,c,d,e,f))
    
        
            
        
