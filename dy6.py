def miss(arr):
    end=max(arr)
    start=min(arr)
    total=end*(end+1)//2-start*(start-1)//2
    actual=sum(arr)
    missing=total-actual
    print(missing)
arr=list(map(int,input("enter the elements: ").split()))
miss(arr)