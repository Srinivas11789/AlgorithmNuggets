class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # alternative small solution from discussions
        
        # Given a list of integers, use set to eradicate duplicates
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return list(nums1 & nums2)
        

        """
        str1 = "".join(str(i) for i in nums1) 
        str2 = "".join(str(i) for i in nums2)
        if str1 == str2:
            return map(int,str1)
        elif str1 == "" or str2 == "":
            return []
        #if str2 in str1:
        #    return map(int,str1[str1.index(str2)])
        else:
            result = set()
            for num in nums1:
                if num in nums2:
                    result.add(num)
            return list(result)
        """
