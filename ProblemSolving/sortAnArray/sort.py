class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Inbuilt function
        ## return sorted(nums)
        
        # Quick sort
        def quickSort(array):
            less = []
            equal = []
            greater = []
            if len(array) > 1:
                pivot = array[0]
                for i in array:
                    if i < pivot:
                        less.append(i)
                    elif i == pivot:
                        equal.append(i)
                    else:
                        greater.append(i)
                return quickSort(less)+equal+quickSort(greater)
            else:
                return array
        return quickSort(nums)
        
        # Merge sort way
        """
        def mergeSort(array):
            if len(array) > 1:
                n = len(array)//2
                left = array[:n]
                right = array[n:]
                
                mergeSort(left)
                mergeSort(right)
                
                i = j = k = 0
                
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        array[k] = left[i]
                        i += 1
                    else:
                        array[k] = right[j]
                        j += 1
                    k += 1
                
                while i < len(left):
                    array[k] = left[i]
                    i += 1
                    k += 1
                
                while j < len(right):
                    array[k] = right[j]
                    j += 1
                    k += 1
            
            return array
        
        mergeSort(nums)
        return nums
        """
        
        
