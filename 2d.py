r=2
c=3
arr=[[0 for i in range(c)] for j in range(r)]
print(arr)
ar1=[]
row,col=3,3
for i in range(row):
    cols=[]
    for j in range(col):
        cols.append(0)
    ar1.append(cols)
print(ar1)
ar1[0][1]=92
print(ar1)
for i in ar1:
    for j in i:
        print(j , end=" ")
    print()