def matrix(row,column):
    mat=[]
    for i in range(row):
        cols=[]
        for j in range(column):
            value=int(input(f"enter value for {i}{j}: "))
            cols.append(value)
        mat.append(cols)
    return mat
def show(mat):
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()
def add(mat):
    sum=0
    for i in mat:
        for j in i:
            sum+=j
    print(sum)
row=int(input("enter number of rows: "))
column=int(input("enter number of columns: "))
mat=matrix(row,column)
show(mat)
add(mat)