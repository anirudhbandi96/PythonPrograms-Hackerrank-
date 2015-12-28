a=[]
a.append(list(raw_input()))
a.append(list(raw_input()))
z=list(set(a[0]))
x=list(set(a[1]))
#print(z)
#print(x)
count=0
for i in z:
    #print(i)
    if i not in x:
        #print('element of z not in x')
        count+=a[0].count(i)
        #print(count)
    else:
        #print('element of z in x')
        if a[0].count(i)!=a[1].count(i):
            #print('in x but..',abs(a[0].count(i)-a[1].count(i)))
            count=count+abs(a[0].count(i)-a[1].count(i))
            #print(count)
for i in x:
    if i not in z:
        #print('element of x not in z')
        count+=a[1].count(i)
        #print(count)
print(count)       
                      
