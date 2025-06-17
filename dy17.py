def dup(arr):
    seen=set()
    duplicate=set()
    for i in arr:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)
    return list(duplicate)
arr=list(map(int,input("enter elements: ").split()))
print(dup(arr))