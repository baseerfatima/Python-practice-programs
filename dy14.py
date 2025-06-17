def maj(arr):
    n=len(arr)
    dic={}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in dic:
        if dic[i]>n/2:
            print(i)
arr=[2,2,1,2,2]
maj(arr)