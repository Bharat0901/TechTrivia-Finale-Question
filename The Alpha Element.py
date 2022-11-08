def primen(n):
    p=0
    a=[int(s) for s in str(n)]
    for w in a:
        if w in [0,1,2,3,5,7]: p+=1
    return p

t=int(input("Enter the no of test cases "))
for _ in range(t):
    n=int(input("enter the length of the arr "))
    arr=[]
    p=[]
    for _ in range(n):
        inp=int(input("Ele "))
        arr.append(inp)
        if str(inp)==str(inp)[::-1]: p.append(inp)
    arr1=[]
    X=[]
    for j in arr:
        temp=[int(x) for x in str(j)]
        arr1.append(temp)
    for q in arr1:
        l=len(q)
        m=max(q)
        if l%2==0:
            if q[:l//2]==q[(l//2):]:
                dat=(l)*(m-min(q))*(m**3)
                dat=str(dat)[::-1]
                X.append(int(dat))
        else:
            if q[:l//2]==q[(l//2)+1:]:
                dat=(l+q[(l//2)])*(m-min(q))*(m**3)
                dat=str(dat)[::-1]
                X.append(int(dat))
    Sx=sum(X)
    sp=sum(p)
    pmin=min(p)
    fx=Sx-(pmin*sp)
    if fx>0: fx=fx+69
    else:
        s="69"
        while fx<0:
            tempp=fx+int(s)
            if tempp>0:
                fx=tempp
                break
            s=s+"69"
    for e in range(len(p)): p[e]=p[e]*fx
    d={}
    for prime in p:
        e1=primen(prime)
        if e1 not in d: d[e1]=[prime]
        else: d[e1]+=[prime]
    maxp=max(d)
    tempsum=[]
    flag=0
    for ex in d[maxp]:
        if len(d[maxp])>1:
            data87=[int(h) for h in str(ex)]
            tempsum.append([sum(data87),ex])
            flag=1
        else: tempsum=ex 
    if flag==0: print("the Alpha element is ", tempsum[0])
    else: print("the Alpha element is ", max(tempsum)[1])