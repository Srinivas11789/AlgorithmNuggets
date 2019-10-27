class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        n = len(nums)
        i = 0
        while i < len(nums):
            count = 1
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                nums.pop(j)
                count += 1
            if count <= n//3:
                nums.pop(i)
            else:
                i += 1
            print(nums, i, j)
        return nums
