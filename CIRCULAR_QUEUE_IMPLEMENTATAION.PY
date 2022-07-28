#CIRCULAR QUEUE IMPLEMENTATION
class circularqueue():
    def __init__(self,maxsize):
        self.queue=list()
        self.maxsize=maxsize
        self.head=0
        self.tail=0
    def enqueue(self,data):
        if self.size() == (self.maxsize-1):
            return("QUEUE IS FULL")
        else:
            self.queue.append(data)
            self.tail=(self.tail+1)%self.maxsize
            return True
    def dequeue(self):
        if self.size()==0:
            return("QUEUE IS EMPTY.")
        else:
            data=self.queue[self.head]
            self.head=(self.head+1)%self.maxsize
            return data
    def size(self):
        if self.tail >= self.head:
            qsize=self.tail-self.head
        else:
            qsize=self.maxsize-(self.head-self.tail)
        return qsize
#size=input("ENTER SIZE OF CIRCULAR QUEUE: ")
#q=circularqueue(int(size))
q=circularqueue(int(9))
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))
print(q.enqueue(60))
print(q.enqueue(70))
print(q.enqueue(80))
print("THE QUEUE SIZE: ")
print(q.size())
print("THE DEQUEUED ELEMENTS: ")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print("THE QUEUE SIZE: ")
print(q.size())
