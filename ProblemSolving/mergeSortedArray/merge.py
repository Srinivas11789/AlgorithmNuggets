# NAIVE LOGIC PENDING
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        """
        # 100pass -- Pythonic version with sort()
        # Difference between sorted() and .sort()
        # 1. sorted() - return a new sorted list with the elements, works on all datastructures like dict, list and tuples
        # 2. .sort() - mutates the list into sorted ones - less space and faster
        # https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort
        
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        """
        
        """
        # Naive logic - doesnt work well with zeros in list 
        for num in nums2: 
            i = 0
            while i < m+n:
                if num <= nums1[i] and nums1[i] != 0:
                    j = (m+n)-1
                    while j > i:
                        nums1[j] = nums1[j-1]
                        j -= 1
                    nums1[i] = num
                    break
                elif nums1[i] == 0 and i >= m:
                    nums1[i] = num
                    break
                i += 1
        """
            
                        
                    
            
            
            
      
