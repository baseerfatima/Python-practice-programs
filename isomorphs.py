def iso(str1,str2):
    if len(str1)!=len(str2):
        return False
    dic1_2={}
    dic2_1={}
    for i,j in zip(str1,str2):
        if i in dic1_2:
            if dic1_2[i]!=j:
                return False
        dic1_2[i]=j 
        if j  in dic2_1:
            if dic2_1[j]!=i:
                return False
        dic2_1[j]=i
    return True
str1=input("enter string 1: ")
str2=input("enetr string 2: ")
print(iso(str1,str2))