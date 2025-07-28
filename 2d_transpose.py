def transpose(mat):
    row=len(mat)
    col=len(mat[0])
    t_mat=[]
    for i in range(col):
        rows=[]
        for j in range(row):
            val=mat[j][i]
            rows.append(val)
        t_mat.append(rows)
    return t_mat
r=int(input("enter the number of rows: "))
c=int(input("enter the number of columns: "))
mat=[]
for i in range(r):
    rows=[]
    for j in range(c):
        val=int(input(f"enter the value of {i+1} row and {j+1} column: "))
        rows.append(val)
    mat.append(rows)
print(transpose(mat))

        