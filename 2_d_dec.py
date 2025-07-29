def check(mat):
    rows=len(mat)
    cols=len(mat[0])
    for i in range(cols):
        for j in range(rows-1):
            if mat[j][i]>mat[j+1][i]:
                return False
    return True

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