def count(arr):
    dic={}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in dic:
        if dic[i]>1:
            print(i)
arr=list(map(int,input("enter elements: ").split()))
count(arr)
