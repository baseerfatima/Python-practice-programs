def insertion(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
nums=list(map(int,input("enter the numbers to be sorted: ").split(",")))  
insertion(nums)
print("after sorting: ", nums)
    
