def matrix(row,col):
    mat=[]
    for i in range(row):
        cols=[]
        for j in range(col):
            val=int(input(f'enter value for {i} {j}: '))
            cols.append(val)
        mat.append(cols)
    return mat
def row_sum(mat):
    r=len(mat)
    c=len(mat[0])
    row_sum_list=[]
    for i in range(r):
        sum=0
        for j in range(c):
            sum+=mat[i][j]
        row_sum_list.append(sum)
    return row_sum_list
def col_sum(mat):
    r=len(mat)
    c=len(mat[0])
    col_sum_list=[]
    for i in range(c):
        sum=0
        for j in range(r):
            sum+=mat[j][i]
        col_sum_list.append(sum)
    return col_sum_list
row=int(input("enter no of rows: "))
col=int(input("enter number of colums: "))
mat=matrix(row,col)
print(col_sum(mat))
