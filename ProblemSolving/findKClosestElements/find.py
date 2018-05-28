class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        # Control Variables
        i = 0
        n = len(arr)
        result = []
        
        
        # Out of Bounds condition - when x lies outside the array list
        if x < arr[0] or x > arr[n-1]:
            if (arr[0]-x) > (arr[n-1]-x):
                return arr[-k:]
            else:
                return arr[:k]
        
        # In Bound - when x lies inside the array
        # When x is a element in the array itself
        if x in arr:
            index = arr.index(x)
        else:
            # When x lies inside the array but not present in the array, select the closest element of x in array
            j = 0
            index = None
            while index == None:
                j += 1
                if x-j in arr:
                    index = arr.index(x-j)
                elif x+j in arr:
                    index = arr.index(x+j)
        
        # Control variables
        print index
        count, left, right = 0, index-1, index+1
        
        # Append the selected index and increment count
        result.append(arr[index])
        count += 1
        
        
        # Iterate with left and right pointers to the selected index, appending the closest element to k
        while left >= 0 and right < n:
            leftDiff = x - arr[left] 
            rightDiff = arr[right] - x
            #print leftDiff, rightDiff, arr[left], arr[right]
            if leftDiff <= rightDiff:
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            count += 1
            if count == k :
                break
            #print result
        
        # Until exhaustion if count < k over the left
        while count < k and left >= 0:
            result.append(arr[left])
            left -= 1
            count += 1
            if count == k :
                break
        
        # Until exhaustion if count < k over the right
        while count < k and right < n:
            result.append(arr[right])
            right += 1
            count += 1
            if count == k :
                break
        
        """
        # add by distance or closest
        while i >= 0:
                result.append(arr[i])
                count += 1
                if count == k:
                    break
                i -= 1
        i = index
        while count < k:
                i += 1
                result.append(arr[i])
                count += 1
        """
        
        return sorted(result)
        
    
        
        
        """
        while i < n:
            if x < 0:
                result.append(arr[i]+x)
            else:
                result.append(abs(arr[i]-x))
            i += 1
        print result
        """
        
        # K is always valid smaller than the array
        #return arr[result:result+k]
            
                
            
            
         
