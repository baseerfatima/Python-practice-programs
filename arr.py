def sum(arr):
    even=[]
    odd=[]
    for i in range(len(arr)):
        if i %2==0:
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort()
    if len(even) >1:
        sec_even=even[-2]
    else:
        sec_even=even[-1]
    if len(even) >1:
        sec_odd=odd[-2]
    else:
        sec_odd=odd[-1]
    return sec_even+sec_odd

arr=list(input("enter the array elements: "))
res=sum(arr)
print(res)
