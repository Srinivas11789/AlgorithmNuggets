class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # We dont want a dictionary to loose the increasing property, use list to increase incrementally, so we maintain an time list
        self.data = {}
        self.times = []
        
    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        # Technically we do not need the key
        self.times.append(timestamp)
        if key not in self.data:
            self.data[key] = [[],[]]
        self.data[key][0].append(timestamp)
        self.data[key][1].append(value)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        
        # Implement binary search to search the element close to this
        """
        n = len(self.data)
        left, right = 0, n
        while left <= right:
            mid = left+(right-1)//2
            if self.data[mid][0] == timestamp:
                return 
            elif self.data[mid][0] < timestamp:
                right = mid
            else:
                left = mid
        """

        #print(self.data, left, right, timestamp)
        
        import bisect
        def binary_search(array, x):
            #print(array, x)
            index = bisect.bisect_left(array, x)
            #print(index)
            if index < len(array) and array[index] == x:
                return index
            elif index:
                return (index-1)
            else:
                return -1
            
        #index = binary_search(self.times, timestamp)
        #print(index)
        
        # Naive Iteration - Time Limit Exceeded
        """
        for i in range(len(self.data)-1, -1, -1):
            if self.data[i][0] <= timestamp and key == self.data[i][1]:
                #print(self.data[i][2])
                return self.data[i][2]
        return ""
        """
        
        # Naive iteration with dictionary
        if key not in self.data:
            return ""
        
        #data = sorted(self.data[key], key=lambda x:x[0], reverse=True)
        #data = self.data[key]
        """
        for val in data:
            if val[0] <= timestamp:
                return val[1]
        """
        times = self.data[key][0]
        index = binary_search(times, timestamp)
        #print(index)
        if index == -1:
            return ""
        else:
            return self.data[key][1][index]
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
