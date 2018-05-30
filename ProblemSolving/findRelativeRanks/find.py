class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        # Logic
        # Ranks dictionary to hold the relative ranking, which is formed by comparing the nums array in a reverse sorted form
        ranks = {}
        snums = sorted(nums)[::-1]
        for i in range(len(snums)):
            if snums[i] not in ranks:
                ranks[snums[i]] = 0
            ranks[snums[i]] = i+1
        
        # Iterate the array to form the relation with ranks dict and create the result 
        result = []
        for num in nums:
            if ranks[num] == 1:
                result.append("Gold Medal")
            elif ranks[num] == 2:
                result.append("Silver Medal")
            elif ranks[num] == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(ranks[num]))
        return result
                
        """
        # Brute - wrong method - result array index to be maintained
        score = sorted(nums)[::-1]
        result = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result.extend([str(i+4) for i in range(len(nums[3:]))])
        return result
        """
