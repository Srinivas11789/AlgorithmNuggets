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


"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        count = 1
        temp = 0
        i = 1
        k = len(nums)
        while i < len(nums):
            if nums[i] == nums[temp]:
                count += 1
                nums.pop(i)
            else:
                if count > k//3:
                    temp = temp + 1
                else:
                    nums.pop(temp)
                i = temp+1
                count = 1
            #print(count, i, temp, nums)
        if temp < len(nums) and count <= k//3:
            nums.pop(temp)
        return nums
"""
