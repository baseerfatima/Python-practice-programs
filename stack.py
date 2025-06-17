class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def isempty(self):
        if len(self.stack) is None:
            return True
    def pop(self):
        if self.isempty():
            print("empty stack")
        else:
            return self.stack.pop()
    def peek(self):
        if self.isempty():
            print("empty stack")
        else:
            return self.stack[-1]
    def lenght(self):
        return len(self.stack)

s=stack()
s.push(10)
s.push(12)
s.push(55)
print(s.pop())
print(s.lenght())
print(s.peek())

            