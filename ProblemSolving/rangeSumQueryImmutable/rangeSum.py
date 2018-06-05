class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        # Subtraction - not working
        #self.sum = sum(nums)
        
        # As the function is called again and again number of times causing time limit exceed lets memoize
        # Memoization will be with respect to j value - > 0sum, 1sum, 2sum ....
        sumi = 0
        self.memo = []
        for i in range(len(self.nums)):
                sumi += self.nums[i]
                self.memo.append(sumi)
        print self.memo

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i-1 >= 0:
            return self.memo[j] - self.memo[i-1]
        else:
            return self.memo[j]
        
        """
        # Time Limit Exceeded Logic - Addition
        self.sum = 0
        for k in range(i,j+1):
            self.sum += self.nums[k]
        return self.sum
        """
        
        """
        # Time Limit Exceeded Logic - Subtraction
        temp = self.sum
        for k in range(len(self.nums)):
            if k not in range(i,j+1):
                temp -= self.nums[k]
        return temp
        """
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
