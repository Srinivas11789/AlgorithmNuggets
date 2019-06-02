class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        """
        # O(smaller_array) iteration - 30% faster
        n = len(nums1)
        m = len(nums2)
        result = []
        for i in range(n):
            if nums1[i] in nums2 and nums1[i] not in result:
                result.append(nums1[i])
        return result
        """
        
        """
        # Logic 1: Set intersection ( set vs set ) - 83% faster
        nums1 = set(nums1)
        nums2 = set(nums2)
        return nums1.intersection(nums2)
        """
    
        """
        # Logic 2: Set intersection ( set vs list ) - 72% faster
        nums1 = set(nums1)
        return nums1.intersection(nums2)
        """
        
        """
        # Logic 3: Dictionary Method - 77% faster
        import collections
        dic = collections.Counter(list(set(nums1))+list(set(nums2)))
        result = []
        for k,v in dic.items():
            if v >= 2 and k not in result:
                result.append(k)
        return result
        """
        
        # Logic 4: Binary Search
        
        
        
