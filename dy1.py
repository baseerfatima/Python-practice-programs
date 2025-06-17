n="abcaabc"
dic={}
for i in n:
    if i in dic:
        dic[i] +=1
    else:
        dic[i]=1
sorted_dic=sorted(dic.items(), key=lambda x: (-x[1], x[0]))
res=" "
for char, count in sorted_dic:
    res += char*count
print(res)


