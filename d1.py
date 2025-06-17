def ans(*args):
    return sum(map(float,args))
def chechk(*args):
       try:
             list(map(float,args))
             return True
       except ValueError:
             return False
def add_nums(*args):
      if not chechk(*args):
            return "error"
      else:
            return ans(*args)

n=input()
args=n.split()
print(add_nums(*args))
