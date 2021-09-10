class MyHashMap:
    
    # Logic 1: using lists for key and values with reusing uniq indexes to relate key/value pairs --> 5% faster 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # using lists to implement hashmap
        self.keys = []
        self.values = []
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for k in range(len(self.keys)):
            if self.keys[k] == key:
                self.values[k] = value
                return
        self.keys.append(key)
        self.values.append(value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for k in range(len(self.keys)):
            if self.keys[k] == key:
                return self.values[k]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for k in range(len(self.keys)):
            if self.keys[k] == key:
                self.keys = self.keys[:k] + self.keys[k+1:]
                self.values = self.values[:k] + self.values[k+1:]
                return
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
