class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # Write more with BST Tree of internals of a dictionary
        
        # Logic 1: With Dictionary
        # HashSet principles from references
        # * Summary
        #   - Set contains only unique values
        #   - Internally its a dictionary with element as key and dummy value or present as value
        #   - Returns null when key is unique and added, else the value if already present
        # * https://javahungry.blogspot.com/2013/08/how-sets-are-implemented-internally-in.html
        self.ds = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.ds:
            return
        self.ds[key] = "present"
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.ds:
            del self.ds[key]

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.ds:
            return True
        else:
            return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
