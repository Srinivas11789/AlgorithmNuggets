class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        result = [[],[]]
        
        count_nums1 = {}
        for i in nums1:
            if i not in count_nums1:
                count_nums1[i] = 0
            count_nums1[i] = 1
            
        count_nums2 = {}
        for i in nums2:
            if i in count_nums1:
                count_nums1[i] -= 1
                continue
            if i not in count_nums2:
                result[1].append(i)
            count_nums2[i] = 1
        
        for k,v in count_nums1.items():
            if v > 0:
                result[0].append(k)
                
        return result
