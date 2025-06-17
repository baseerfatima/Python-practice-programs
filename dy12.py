def rotate(arr,k):
    new=arr[-k:] + arr[:-k]
    print(new)
arr=[1,2,3,4,5]
k=2
rotate(arr,k)