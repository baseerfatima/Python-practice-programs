def check(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return True
    return False
arr=list(map(int,input("enter array : ").split()))
target=int(input("enter target: "))
print(check(arr,target))
