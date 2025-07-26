from collections import Counter
def chechk(num):
    dic=Counter(num)
    for i in num:
        if dic[i]>1:
            return True
def check(num):
    if len(num)!=len(set(num)):
        return True
