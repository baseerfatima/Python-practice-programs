def trans(invest,k):
    invest.sort()
    diff=invest[-1]-invest[0]
    small_invest=invest[0]+k
    largest_invest=invest[-1]-k
    