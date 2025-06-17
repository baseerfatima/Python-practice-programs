def maxsub(arr):
    max_sum=float("-inf")
    curr=0
    for i in arr:
        curr+=i
        max_sum=max(curr,max_sum)
        if curr<0:
            curr=0
    return max_sum
a=[1,2,3,-4,5,6,7]
print(maxsub(a))