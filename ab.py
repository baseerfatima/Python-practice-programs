def a(n,d):
    count=0
    for i in range(1,n):
        if d[i] !=d[i-1]:
            count+=1
    return count
n=int(input("no of friends: "))
d=list(input("enetr the elements: "))
res=a(n,d)
print(res)