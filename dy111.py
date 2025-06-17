def chec(arr,target):
    seen=set()
    for i in arr:
        needed=target-i
        if needed in seen:
            return True
        else:
            seen.add(i)
arr=[2,7,9,11]
target=9
print(chec(arr,target))