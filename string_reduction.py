z=[]
def func(i):
    if(set(i)==1):
        return len(i)
    else:
        g=len(i)
        h=[]
        if "ab" in i:
            print(i)
            f=(i.replace("ab","c"))
            if len(f)<=g:
                g=len(f)
                h=f
        elif "ba" in i:
            print(i)
            a=(i.replace("ba","c"))
            if len(a)<=g:
                g=len(a)
                h=a
        elif "ac" in i:
            print(i)
            b=(i.replace("ac","b"))
            if len(b)<=g:
                g=len(b)
                h=b
        elif "ca" in i:
            print(i)
            c=(i.replace("ca","b"))
            if len(c)<=g:
                g=len(c)
                h=c
        elif "bc" in i:
            print(i)
            d=i.replace("bc","a")
            if len(d)<=g:
                g=len(d)
                h=d
        elif "cb" in i:
            print(i)
            e=(i.replace("cb","a"))
            if len(e)<=g:
                h=e
        return func(h)
    
for i in range(int(input())):
    z.append(input())
for i in z:
    func(i)
