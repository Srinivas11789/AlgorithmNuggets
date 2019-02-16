class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # One line hack using sorted method - 97%
        #return sorted(nums, reverse=True)[k-1]
        
        # Merge Sort and Select - 30%
        def mergeSort(arr):
            if len(arr) > 1:
                #print arr
                # Divide the array
                n = len(arr)//2

                # Split array into left and right
                left = arr[:n]
                right = arr[n:]

                # Recursive call
                mergeSort(left)
                mergeSort(right)

                i = j = k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                
                return arr
            else:
                return arr
            
        return mergeSort(nums)[-k]
            
            
            
        
