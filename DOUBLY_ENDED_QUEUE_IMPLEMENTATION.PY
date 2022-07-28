#DOUBLE ENDED QUEUE IMPLEMENTATION
class dequeue:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items == []
    def addrear(self,item):
        self.items.append(item)
    def addfront(self,item):
        self.items.insert(0,item)
    def removefront(self):
        return self.items.pop(0)
    def removerear(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
d=dequeue()
print(d.isempty())
d.addrear(8)
d.addrear(5)
d.addrear(7)
d.addrear(0)
print(d.items)
print(d.size())
print(d.isempty())
d.addrear(11)
print(d.items)
print(d.removerear())
print(d.items)
print(d.removefront())
print(d.items)
d.addfront(55)
d.addrear(45)
print(d.items)
print(d.size())
