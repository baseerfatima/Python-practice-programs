def sub(s,t):
    i,j=0,0
    while i < len(s)  and j < len(t):
        if s[i]==t[j]:
            i+=1
        j+=1
    return i==len(s)
str1=input("enter the string: ")
str2=input("enter the subseq to be checked: ")
print(sub(str2,str1))
