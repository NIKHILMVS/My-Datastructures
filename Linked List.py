class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class Solution:
    def __init__(self):
        self.head=None
    
    def printAll(self):
        v=self.head
        while(v):
            print(v.val)
            v=v.next
    
    def printAllReverse(self):
        v=self.head
        while(v.next!=None):
            v=v.next
        while(v):
            print(v.val)
            v=v.prev
    def insertAtStart(self,data):
        if self.head==None:
            n=Node(data)
            self.head=n
        else:
            n=Node(data)
            n.next=self.head
            self.head.prev=n
            self.head=n
            v=self.head
        
    def insertInBetween(self,prevnode,data):
        n=Node(data)
        if prevnode.next==None:
            prevnode.next=n
            n.prev=prevnode
        else:
            n.next=prevnode.next
            prevnode.next.prev=n
            n.prev=prevnode
            prevnode.next=n
            
    def insertAtEnd(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            n=Node(data)
            v=self.head
            while(v.next!=None):
                v=v.next
            v.next=n
            n.prev=v
    
    def delete(self,data):
        n=Node(data)
        v=self.head
        while(v!=None):
            if v.val==n.val:
                if v.next==None:
                    v.prev.next=None
                    return
                elif v.prev==None:
                    self.head=v.next
                    v.next.prev=None
                    return
                else:
                    v.prev.next=v.next
                    v.next.prev=v.prev
                    return
            v=v.next
        return "Not Found"
    
    def search(self,data):
        n=Node(data)
        v=self.head
        cnt=0
        while(v!=None):
            if v.val==n.val:
                return f"the value '{v.val}' found at index {cnt}"
            cnt+=1
            v=v.next
        return "Not Found"
        
        
        
        
sol=Solution()

n1=Node(5)
n2=Node(6)
n3=Node(7)
n4=Node(8)
n5=Node(9)
n6=Node(10)

sol.head=n2.prev=n1
n1.next=n3.prev=n2
n2.next=n4.prev=n3
n3.next=n5.prev=n4
n4.next=n6.prev=n5
n5.next=n6


sol.insertInBetween(n2,100)
sol.insertAtEnd(999)
sol.delete(7)
print(sol.search(6))
sol.printAll()
sol.printAllReverse()
