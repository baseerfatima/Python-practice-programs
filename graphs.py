class graph:
    def __init__(self):
        self.g={}
    def insertedges(self,u,v):
        if u not in self.g:
            self.g[u]=set()
        self.g[u].add(v)
    def remove(self,u,v):
        if u in self.g and v in self.g[u]:
            self.g[u].remove(v)
    def display(self):
        for i in self.g:
            print(f"{i}->{self.g[i]}")

a=graph()
a.insertedges(10,7)
a.insertedges(10,8)
a.display()
