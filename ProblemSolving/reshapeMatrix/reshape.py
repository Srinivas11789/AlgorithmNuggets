class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        total = r*c
        all_elements = []
        # all nums
        for num in nums:
            all_elements.extend(num)
        
        result = []
        if total > len(all_elements):
            return nums
        else:
            for i in range(r):
                current = []
                for j in range(c):
                    if j < len(all_elements):
                        current.append(all_elements[j])
                result.append(current)
                all_elements = all_elements[c:]
        
        return result
