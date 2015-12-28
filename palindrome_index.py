import math
a=[]
for p in range(int(input())):
    i=input()
    if(i!=i[len(i)::-1]):
        for j in range(len(i)):
            s=i[:j]+i[j+1:]
            #print('p',p)
            #print('s',s)
            #print('fhs',s[:int(len(s)/2)])
            #print('shs',s[len(s):math.ceil(len(s)/2)-1:-1])
            if(s[:int(len(s)/2)]==s[len(s):math.ceil(len(s)/2)-1:-1]):
                #print('entered loop')
                a.append(j)
                break
    else:
        a.append(-1)
for k in a:
    print(k)
