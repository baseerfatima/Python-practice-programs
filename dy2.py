def non(n):
    dics={}
    for i in n :
        if i in dics:
            dics[i]+=1
        else:
            dics[i]=1
    for char in n:
        if dics[char]==1:
            print(char)
            return
    print(None)
n="aabccdef"
non(n)

