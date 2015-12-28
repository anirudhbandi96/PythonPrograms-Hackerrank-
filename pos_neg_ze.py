a=int(input())
p=n=z=0
for i in (list(map(int,input().split()))):
    if i>0:
        p+=1
    elif i<0:
        n+=1
    else:
        z+=1
print(p/a)
print(n/a)
print(z/a)
