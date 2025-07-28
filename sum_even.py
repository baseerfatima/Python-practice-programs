def sum_even(lis1):
    sum=0
    for i in lis1:
        if i%2==0:
            sum+=i
    print(sum)

sum_even([2,4,5,6,7])