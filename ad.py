def find(arr,len,num,diff):
    count=0
    for i in range(len):
        if abs(arr[i]-num)<=diff:
            count+=count
    return count

len=int(input("enter the size of array: "))
arr=list(input("array: "))
num=int(input("enter number: "))
diff=int(input("enter diff: "))
res=find(arr,len,num,diff)
print(res)