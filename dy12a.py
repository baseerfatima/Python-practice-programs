def rev(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

def rotate(arr,k):
    if k>len(arr):
        k=k%len(arr)
    rev(arr,0,len(arr)-1)
    rev(arr,0,k-1)
    rev(arr,k,len(arr)-1)
    return arr
arr=[1,2,3,4,5]   
k=2
print(rotate(arr,k))
