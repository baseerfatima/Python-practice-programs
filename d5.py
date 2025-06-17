def second_most(n):
    dic={}
    for i in n:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    list_sorted=sorted(dic.items(), key=lambda x: -x[1])
    if len(list_sorted)<2:
        print("no second most")
    else:
        print(list_sorted [1][0])
n=input("enter: ")
second_most(n)
