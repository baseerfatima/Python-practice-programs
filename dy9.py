def second(arr):
    largest=second=float('-inf')
    for i in arr:
        if i>largest:
            second=largest
            largest=i
        elif i>second and i!=largest:
            second=i
    print(second)
arr=list(map(int,input(" ").split()))
second(arr)
