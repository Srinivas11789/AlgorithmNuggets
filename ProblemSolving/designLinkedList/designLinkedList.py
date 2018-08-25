"""
# using only list operation
# Only List Operation
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkedList = []
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        n = len(self.linkedList)
        if index < 0 or index >= n or self.linkedList == []:
            return -1
        else:
            return self.linkedList[index]
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.linkedList = [val] + self.linkedList
        
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.linkedList.append(val)
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == len(self.linkedList):
            self.addAtTail(val)
        elif index > len(self.linkedList):
            pass
        else:
            self.linkedList = self.linkedList[:index]+[val]+self.linkedList[index:]
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        self.linkedList = self.linkedList[:index]+self.linkedList[index+1:]
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
"""

## Linked List Object method backed up by list data structure
### Works a little hacky - comments pending

# Hacky Linked List Method
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkedList = []
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        n = len(self.linkedList)
        if index < 0 or index >= n or self.linkedList == []:
            return -1
        else:
            return self.linkedList[index]["val"]
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = {}
        node["val"] = val
        node["prev"] = None
        if self.linkedList:
            node["next"] = self.linkedList[0]
            self.linkedList[0]["prev"] = node
        else:
            node["next"] = None
        self.linkedList = [node] + self.linkedList
        
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = {}
        node["val"] = val
        node["next"] = None
        if len(self.linkedList) > 0:
            node["prev"] = self.linkedList[len(self.linkedList)-1]
            self.linkedList[len(self.linkedList)-1]["next"] = node
        else:
            node["prev"] = None
        self.linkedList.append(node)
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == len(self.linkedList):
            self.addAtTail(val)
        elif index > len(self.linkedList):
            pass
        else:
            node = {}
            node["val"] = val
            node["next"] = self.linkedList[index]
            node["prev"] = self.linkedList[index-1]
            self.linkedList = self.linkedList[:index]+[node]+self.linkedList[index:]
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= 0 and index < len(self.linkedList):
            self.linkedList = self.linkedList[:index]+self.linkedList[index+1:]
            #print self.linkedList, index
            if index-1 == len(self.linkedList)-1:
                self.linkedList[index-1]["next"] = None
            elif index-1 == 0:
                self.linkedList[index-1]["next"] = None
                self.linkedList[index]["prev"] = None
            elif index-1 > 0:
                self.linkedList[index-1]["next"] = self.linkedList[index]
                self.linkedList[index]["prev"] = self.linkedList[index-1] 
            else:
                self.linkedList[index-1]["prev"] = None
    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
