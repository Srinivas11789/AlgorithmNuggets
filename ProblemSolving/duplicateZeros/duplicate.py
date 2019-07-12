class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        # Logic1: Lousy method: 100 pass 5% faster
        # * At every 0 hit, shift all the elements and add zero
        """
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
        """
        
        # Logic2: Similar to 2 pointer method - 100 pass 97 % faster
        # * We could count the zeros (shift) that will fit the array
        # * Use the remaining array to make the changes

        n = len(arr)
        
        # Count the Number of shifts - I altered this to store appropriate positions
        shift_indices = [] # Indices where shift should happen
        shift = 0 # Count the shift required as we iterate
        shift_index = 0 # The index that would be the end of array in the future shifted array
        for i in range(n):
            shift += 1 # Shift for every element
            if shift == n: # If shift cover the array return the shift index
                shift_index = i
                break
            elif arr[i] == 0: # Extra shift for 0s
                shift_indices.append(i)
                shift += 1
            if shift == n: # If shift cover the array return the shift index ( after extra shift)
                shift_index = i
                break
        # print shift, shift_index, arr, shift_indices
        
        # The real index in the array
        real_index = n-1
        # The next shift index
        if shift_indices:
            next_shift = shift_indices.pop()
        else:
            next_shift = None
        # Shifting... by one iteration
        while shift_index >= 0 and real_index >= 0:
                arr[real_index] = arr[shift_index] # Shift for all the elements
                if shift_index == next_shift: # Add extra 0s in place for next shift element
                    arr[real_index-1] = 0
                    real_index -= 1 # Extra iteration for extra 0
                    # Update the next shift
                    if shift_indices:
                        next_shift = shift_indices.pop()
                    else:
                        next_shift = None
                # Iterate and reduce indices
                shift_index -= 1
                real_index -= 1
        
        """
        # Uncleaned attempt
        n = len(arr)
        shift_indices = []
        shift = 0
        shift_index = 0
        for i in range(n):
            shift += 1
            if shift == n:
                shift_index = i
                break
            elif arr[i] == 0:
                shift_indices.append(i)
                shift += 1
            if shift == n:
                shift_index = i
                break
        print shift, shift_index, arr, shift_indices
        real_index = n-1
        if shift_indices:
            next_shift = shift_indices.pop()
        else:
            next_shift = None
        while shift_index >= 0 and real_index >= 0:
                arr[real_index] = arr[shift_index] 
                if shift_index == next_shift:
                    arr[real_index-1] = 0
                    real_index -= 1
                    if shift_indices:
                        next_shift = shift_indices.pop()
                    else:
                        next_shift = None
                shift_index -= 1
                real_index -= 1
        """
        
