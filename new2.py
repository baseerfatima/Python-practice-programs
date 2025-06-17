def anagram(str1,str2):
    str1=str1.replace(" ", "").lower()
    str2=str2.replace(" ", "").lower()
    li1=list(str1)
    li2=list(str2)
    li1.sort(),li2.sort()
    if li1==li2:
        print("True")
    else:
        print("False")
str1=input("enter word 1: ")
str2=input("enetr word 2 ")
anagram(str1,str2)