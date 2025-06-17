def zeros(arr):
    res=[]
    count=0
    for i in arr:
        if i!=0:
            res.append(i)
        else:
            count+=1
    res.extend([0]*count)
    print(res)
arr=list(map(int,input("enter elements: ").split()))
zeros(arr)