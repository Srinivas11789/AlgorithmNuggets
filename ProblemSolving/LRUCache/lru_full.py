# Essence:
# * We obviously use a dictionary to perform the operations within O(1)
# * To track the least used element we need some sort of arrangement or array to move items accessed to the last
#   - So the first item all the time is the least accessed


# Logic1: OrderedDictionary to move stuff around while maintaining a dictionary - 86% faster
"""
from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = OrderedDict()
        

    def get(self, key):
        if key not in self.dict:    # Key not found in dict
            return -1                
        self.dict.move_to_end(key)  # Move the accessed one to the end
        return self.dict[key]       # Return value
        

    def put(self, key, value):
        if key in self.dict:                # Key in Dictionary then move accessed part
            self.dict.move_to_end(key)
        self.dict[key] = value              # Add key, value to dict
        if len(self.dict) > self.capacity:  # Greater than capacity
            self.dict.popitem(last = False) # Pop the least accessed item


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""

# Logic 2: Using a Dictionary and Double Linked List to achieve the same in naive manner - 49% faster

# Define Double Linked List
# * For ease of access and reference lets maintain dummy nodes for head and tail
class DoubleLinkedList(object):
    def __init__(self):
        self.next = None
        self.prev = None
        self.key = None
        self.value = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        # Capacity and Size
        self.capacity = capacity
        self.size = 0
        
        # Dictionary
        self.dict = {}
        
        # Double Linked List
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        
        # update current node
        node.prev = self.head
        node.next = self.head.next
        
        # update head and next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def move_node_to_end(self, node):
        self.remove_node(node)
        self.add_node(node)
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        node = self.dict.get(key, None)
        if not node:
            return -1
        self.move_node_to_end(node)
        return node.value
    
    def pop_tail(self):
        tail = self.tail.prev
        self.remove_node(tail)
        return tail

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        # Get node from the dictionary
        node = self.dict.get(key)
        
        if not node:
            node = DoubleLinkedList()   # create node
            node.key = key
            node.value = value
            self.dict[key] = node
            self.add_node(node)
            self.size += 1
            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.dict[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.move_node_to_end(node) # Update least accessed



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
