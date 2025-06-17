def majority(arr):
    can=None
    count=0
    for i in arr:
        if count==0:
            can=i
            count=1
        elif i==can:
            count+=1
        else:
            count-=1
    if arr.count(can)>len(arr)/2:
        print("majority element : ", can)
    else:
        print("no majority")
arr=list(map(int,input("enter elements: ").split()))
majority(arr)