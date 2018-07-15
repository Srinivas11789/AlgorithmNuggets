# Pending -- time limit exceeded
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.array = nums
        self.k = k
        self.value = 0
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        # Time Limit Exceeded logic otherwise all passed 
        self.array.append(val)
        if val > self.value or not self.value:
            self.array = sorted(self.array)[::-1]
            self.array = self.array[:self.k]
            self.value = self.array[-1]
        return self.value
    
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
