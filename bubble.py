def buuble_sort(nums):
    n=len(nums)
    for i in range(n-1): #passes= n-1
        swap=False #flag
        for j in range(n-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swap=True
        if swap==False:
            break
    return nums
print(buuble_sort([8,5,4,2]))