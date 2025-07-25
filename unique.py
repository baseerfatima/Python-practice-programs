def first(arr):
    dic={}
    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i,value in enumerate(arr):
        if dic[value]==1:
            return i
    return -1
str=input("enetr a string: ")
print(first(str))
