def anagrams(str1,str2):
    #without libraries 
    dic1={}
    dic2={}
    for i in str1:
        dic1[i]=dic1.get(i,0) + 1
    for j in str2:
        dic2[j]=dic2.get(j,0)+1
    return dic1==dic2
str1="listen"
str2="silent"
print(anagrams(str1,str2))