def  target_sum(arr,target):
    #brute force
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]== target:
                print(i,j)
def hash_target_sum(arr,target):
    #hash map using loop
    dic={}
    all=[]
    for i in range(len(arr)): 
        num=target-arr[i]
        if num in dic:
            all.append((dic[num],i))
        dic[arr[i]]=i
    print(all)
def hash_target_sum_en(arr,target):
    #hash map using enumerate
    dic={}
    all=[]
    for i, value in enumerate(arr):
        num=target-value
        if num in dic:
            all.append((dic[num],i))
        dic[value]=i
    print(all)
arr=list(map(int,input("enter the numebrs: ").split(" ")))
target=int(input("enter the sum: "))
target_sum(arr,target)

