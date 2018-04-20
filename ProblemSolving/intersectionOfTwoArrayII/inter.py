class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # 100 pass - Intersection of the array by iteration and poping element from the array two
        result = []
        for n in nums1:
            if n in nums2:
                result.append(n)
                nums2.pop(nums2.index(n))
        return result
    
        # think about these scenarios
        """
        1.What if the given array is already sorted? How would you optimize your algorithm?
        2.What if nums1's size is small compared to nums2's size? Which algorithm is better?
        3.What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the   memory at once?
        """
        # 3. Solution could be to use a sorted arrays and then iterate one element at a time from both the arrays or to use a dictionary and create the intersection relationship
