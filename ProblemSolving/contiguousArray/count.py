class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Logic 2: With Dict to track counting - 86% faster
        prefix_count = {0:-1}
        maxi, count = 0, 0
        for i,v in enumerate(nums): # Step1: iterate by index and value
            count += (-1 if v == 0 else 1) # Make count 1 for 1 and -1 for 0
            if count in prefix_count:
                maxi = max(maxi, i-prefix_count[count])
            else:
                prefix_count[count] = i # Store immediate index after cont array
        return maxi
        
        # Logic 1: O(N) Loop Iteration
        # * This does not work when position or contiguous rule occur, otherwise for any arrangement might work
        """
        zero = 0
        one = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1
            maxi = max(maxi, min(one,zero))
            print(one, zero, maxi)
        return maxi*2
        """
        
