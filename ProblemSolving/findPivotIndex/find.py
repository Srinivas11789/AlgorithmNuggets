class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        # Brute force logic - correct but Time limit exceeded
        n = len(nums)
        for i in range(n):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
        """
        
        """
        # Iterate front and back at a time - calculate sum and increase the sum towards the shorter sum
        # Lesson of why this did not work ----> Use the sum function only once and try to finish off, look at the last solution
        n = len(nums)
        i = 0
        k = n-1
        if n < 1:
            return -1
        left_sum = nums[i]
        right_sum = nums[k]
        while i != k:
            if left_sum < right_sum:
                i += 1
                left_sum += nums[i]
                if left_sum == right_sum:
                    return i+1
            elif left_sum > right_sum:
                k -= 1
                right_sum += nums[k]
                if left_sum == right_sum:
                    return k-1
            else:
                i += 1
                k -= 1
                left_sum += nums[i]
                right_sum += nums[k]

        return -1
        """
        
        # Think very Short + Simple - 100 pass
        # A very nice solution from discussion - yangshun
        
        left, right = 0, sum(nums)
        for i, n in enumerate(nums):
            right -= n
            if left == right:
                return i
            left += n
        return -1
        
        
