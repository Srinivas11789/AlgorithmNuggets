class Solution(object):
    def mergeSort(self, nums):        
            if len(nums) > 1:
                n = len(nums)
                mid = n//2
                l = nums[:mid]
                r = nums[mid:]
                
                self.mergeSort(l)
                self.mergeSort(r)

                i = j = k = 0

                while i < len(l) and j < len(r):
                    if l[i] < r[j]:
                        nums[k] = l[i]
                        i += 1
                    else:
                        nums[k] = r[j]
                        j += 1
                    k += 1

                while i < len(l):
                    nums[k] = l[i]
                    i += 1
                    k += 1

                while j < len(r):
                    nums[k] = r[j]
                    j += 1
                    k += 1

    def sortArray(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mergeSort(arr)
        return arr
            
        
