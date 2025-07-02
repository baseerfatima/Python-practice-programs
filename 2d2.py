def transpose(mat):
    t_mat=[]
    row=len(mat)
    col=len(mat[0])
    for i in range(col):
        new_row=[]
        for j in range(row):
            new_row.append(mat[j][i])
        t_mat.append(new_row)
    print("after transpose: ")
    for i in t_mat:
        for j in i:
            print(j, end=" ")
        print()
def matrix(r,c):
    mat=[]
    for i in range(r):
        cols=[]
        for j in range(c):
            val=int(input(f"enter value for {i} {j}: "))
            cols.append(val)
        mat.append(cols)
    print("before transpose: ")
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()
    return mat
r=int(input("enter no of rows: "))
c=int(input("enter number of colums: "))
mat=matrix(r,c)
transpose(mat)


