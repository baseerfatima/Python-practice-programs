def fun(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

n=int(input("enter no: "))
r=fun(n)
print(r)