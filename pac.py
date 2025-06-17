def turn(n,p):
    if n%2==0:
        if p<n//2:
            if p%2==0:
                t=p-1
            else:
                t=p-2
        else:
            