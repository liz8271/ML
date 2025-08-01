def check(x: str, file: str):
    x=x.lower()
    words = x.split(' ')
    words.sort()
    d=dict()
    for i in words:
        d[i]=words.count(i)
    f=open(file,'w')
    for i in d:
        f.write(i+ ' '+ str(d[i])+ '\n')
    f.close()