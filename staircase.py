a=input()
if a[-2:]=="PM":
    if int(a[:2])!=12:
        print (str(int(a[:2])+12)+a[2:-2])
    else:
        print (a[:-2])
else:
    if int(a[:2])!=12:
        print (a[:-2])
    else:
        print ('00'+a[2:-2])
