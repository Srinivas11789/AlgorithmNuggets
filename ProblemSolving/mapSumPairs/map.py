class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dic[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        result = 0
        for k,v in self.dic.items():
            if prefix in k[:len(prefix)]:
                result += v
        return result
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
