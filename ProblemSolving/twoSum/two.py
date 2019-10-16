class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        elements = {}
        
        for i in range(len(nums)):
            if nums[i] not in elements:
                elements[nums[i]] = []
            elements[nums[i]].append(i)
            
        for i in range(len(nums)):
            if target-nums[i] in elements:
                sec = target-nums[i]
                if sec == nums[i]:
                    if len(elements[sec]) > 1:
                        return [i, elements[target-nums[i]][1]]
                else:
                    return [i, elements[target-nums[i]][0]]
        return -1
    
        """
        
        elements = {}
        for i in range(len(nums)):
            if target-nums[i] in elements:
                return [i, elements[target-nums[i]]]
            else:
                elements[nums[i]] = i
        return -1
        
