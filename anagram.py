z=[]
for i in range(int(input())):
    z.append(input())
for i in z:
    count=0
    sh=i[int(len(i)/2):]
    fh=i[:int(len(i)/2)]
    if (len(i)%2!=0):
        print(-1)
    else:
        for j in list(set(sh)):
            #print('j',j)
            print('the sh set',list(set(sh)))
            if j not in list(set(fh)):
                #print('not in fh')
                #print('the fh set',list(set(fh)))
                if(sh.count(j)!=1):
                    #print('count>=1')
                    count+=sh.count(j)
                    #print(count)
                else:
                    #print('count==1')
                    count+=1
                    #print(count)
            else:
                #print('in fh')
                #print('the fh set',list(set(fh)))
                if(sh.count(j)>fh.count(j)):
                    #print('count not same')
                    count+=(sh.count(j)-fh.count(j))
                    #print(count)
        print(count)
                
