def dig(n):
    while n%7!=0:
        p=1
        for i in str(n):
            p=p*int(i)
        n=n+p
    return n
n=int(input("enter  a value: "))
print(dig(n))