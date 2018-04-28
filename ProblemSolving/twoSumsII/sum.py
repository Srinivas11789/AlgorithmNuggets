class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        # Obviously time limit exceeded - using set also wont help such that target = 0 and array is [0,0,3,5]
        n = len(numbers)
        # Logic 1: Iterate through the numbers - brute force - until the number is lesser than the target
        for i in range(n):
                for j in range(i+1,n):
                    if numbers[i]+numbers[j] == target:
                        return [i+1,j+1]
        return -1
        """
        
        """
        # Time limit exceeeded
        # Logic 2 - Use the TARGET as an hint to solve
        n = len(numbers)
        for i in range(n):
            other = target - numbers[i]
            if other in numbers[i+1:]:
                #print i+1, numbers[i+1:].index(other)+2+i, i, numbers[i+1:].index(other)
                return [i+1, numbers[i+1:].index(other)+2+i]
        """
        
        # 100 pass - Logic 3: Considering a low and a high and converging the array
        n = len(numbers)
        left = 0
        right = n-1
        for i in range(n):
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        
        
                
                
            
            
            
