def check(mat):
    row=len(mat)
    col=len(mat[0])
    for i in range(row):
        #better:
        if mat[i]!=sorted(mat[i]):
            return False
        else:
            return True
        '''if mat[i]==sorted(mat[i]):
            continue
        else:
            return False
    return True'''
r=int(input("enter the number of rows: "))
c=int(input("enter the number of columns: "))
mat=[]
for i in range(r):
    rows=[]
    for j in range(c):
        val=int(input(f"enter the value of {i+1} row and {j+1} column: "))
        rows.append(val)
    mat.append(rows)
print(check(mat))