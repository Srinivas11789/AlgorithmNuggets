class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # 100 pass
        n = len(nums)
        if nums[n-1] < target:
            return n
        for i in range(n):
            if nums[i] == target:
                return i
            else:
                if nums[i] > target:
                    return i
        
        """
        # 100 pass - alternate solution from discussions <can also be represented as a oneliner>
         result = []
        for num in nums:
            if num < target:
                result.append(num)
        return len(result)
        """
