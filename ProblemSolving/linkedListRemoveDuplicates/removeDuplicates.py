class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head 
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next	

    def removeDuplicates(self,head):
        #Write your code here
        if head is None:
            return head
        values = []
        previous = head
        root = head
        head = head.next
        while head is not None:
            if head.next is None:
                if head.data == root.data:
                    root.next = None
            if head.data in values or previous.data == head.data:
                previous.next = head.next
            else:
                values.append(head.data)
                previous = head
            head = head.next
        return root
      
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)   
head=mylist.removeDuplicates(head)
mylist.display(head);
