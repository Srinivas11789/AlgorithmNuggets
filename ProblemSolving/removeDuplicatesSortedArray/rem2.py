class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        temp = None
        i = 0
        while i < len(nums):
            if temp == None:
                temp = nums[i]
                i += 1
            elif temp == nums[i]:
                #print(nums, nums[i])
                nums.pop(i)
                #print(nums, nums[i])
            else:
                temp = nums[i]
                i += 1
        return len(nums)
