def maximum(mat):
    row=len(mat)
    col=len(mat[0])
    max=mat[0][0]
    for i in range(row):
        for j in range(col):
            if mat[i][j]>max:
                max=mat[i][j]
    print(max)
def matrix(r,c):
    mat=[]
    for i in range(r):
        cols=[]
        for j in range(c):
            val=int(input(f"enter value for {i} {j}: "))
            cols.append(val)
        mat.append(cols)
    return mat
    
r=int(input("enter no of rows: "))
c=int(input("enter number of colums: "))
mat=matrix(r,c)
maximum(mat)

