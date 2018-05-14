#Pending....
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        """
        # Time Limit Exceeded
        n = len(nums)
        nums.sort()
        for i in range(1,n+1):
            #print nums[0],i,nums
            if len(nums) > 0 and nums[0] == i:
                while len(nums) > 0 and nums[0] == i:
                    del nums[0]
                    #print nums
            else:
                nums.append(i)
        return nums
        """
        
        """
        # Time limit exceeded => Use O(1) space and O(N) runtime
        n = len(nums)
        nums = list(set(nums))
        diff = n-len(nums)
        i = 1
        j = i-1
        while i < n+1:
            #print i, nums[j], nums
            if not nums:
                nums.append(i)
            elif i == nums[j]:
                nums.pop(j)
            else:
                nums.append(i)
            i += 1
        return nums
        """
