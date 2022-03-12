# Stack
class Stack(object):
    def __init__(self):
        self.stack=[]

    def insertElement(self,element):
        return self.stack.append(element)

    def removeElement(self):
        if not len(self.stack):
            return None
        return self.stack.pop(0)

    def printStack(self):
        print(self.stack)

S=Stack()
S.insertElement(1)
S.insertElement(5)
S.insertElement(10)

print("after insertion",S.printStack())

stack=S.removeElement()
stack=S.removeElement()
print("after removing",S.printStack())

# Queue
class Queue(object):
    def __init__(self):
        self.queue=[]

    def insertElement(self,element):
        self.queue.append(element)
        return self.queue

    def removeElement(self):
        if not len(self.queue):
            return None
        return self.queue.pop()

    def printQueue(self):
        print(self.queue)

Q=Queue()
Q.insertElement(2)
Q.insertElement(4)
Q.insertElement(6)

print("after inserting queue",Q.printQueue())

Q.removeElement()
Q.removeElement()

print("after removing queue",Q.printQueue())
