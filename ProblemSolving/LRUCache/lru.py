# Logic 2: OrderedDict to the rescue
from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Logic 1: Naive method
# * learning: The important part of this problem is that we maintain a list of accessed items vs inaccessed items, that way we keep track of things. We also should make sure this happens in perfect time complexity
# * In the below logic, Having a list with all accessed items put to the end of the list and the inaccessed ones on the front does not work so perfectly with time complexity and answers
# * maintaining the relation between the list vs dict becomes crucial too...
"""
class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.last_used = []

    def get(self, key):
        if key not in self.cache:
            return -1
        # Rotate array 
        self.last_used.append(key)
        return self.cache[key]
        

    def put(self, key, value):
        if key not in self.cache:
            if len(self.cache.keys()) == self.capacity:
                del self.cache[self.last_used.pop(0)]
            #self.last_used.append(key)
            self.cache[key] = value
        print(self.cache)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
