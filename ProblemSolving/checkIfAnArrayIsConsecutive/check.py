class Solution(object):
    def isConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Logic 1: sort and check diff --> NlogN * N --> 27% faster
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                continue
            return False
        return True
        """
        
        # Logic 2: 2*O(N) iteration with O(N) space --> 31% faster
        num = {}
        mini = float('inf')
        maxi = -float('inf')
        for i in nums:
            if i in num:
                return False
            num[i] = 1
            if i < mini:
                mini = i
            if i > maxi:
                maxi = i
        for i in range(mini, maxi):
            if i not in num:
                return False
        return True
