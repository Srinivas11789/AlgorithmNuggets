class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        # Logic1: Lousy method: 100 pass 5% faster
        # * At every 0 hit, shift all the elements and add zero
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                j = n-1
                while j > i+1:
                    arr[j] = arr[j-1]
                    j -= 1
                if i+1 < n:
                    arr[i+1] = 0
                i += 2
            else:
                i += 1
        
        # Logic2: Pending...
        # * We could count the zeros (shift) that will fit the array
        # * Use the remaining array to make the changes
        """
        n = len(arr)
        count = 0
        shift = 0
        shift_index = 0
        
	# Count the zeros, shift and figure out the shift index
	for i in range(n):
            shift += 1
            if shift == n:
                shift_index = i
                break
            elif arr[i] == 0:
                count += 1
                shift += 1
            print shift, shift_index

	# Iterate once and shift elements 
        real_index = n-1
        while shift_index >= 0 and real_index >= 0:
                arr[real_index] = arr[shift_index] 
                if arr[real_index] == 0:
                    arr[real_index-1] = 0
                    real_index -= 1
                shift_index -= 1
                real_index -= 1
                print arr
        """
