def fib(n):
    li=[0,1]
    for i in range(n-2):
        res=li[-1] + li[-2]
        li.append(res)
    return li
n=int(input("enter no: "))
print(fib(n))