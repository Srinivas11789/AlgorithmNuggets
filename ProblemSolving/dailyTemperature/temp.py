class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        """
        # Brute force solution - time limit exceeded - 2 for loop
        n = len(temperatures)
        result = []
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    break
                if j == n-1:
                    result.append(0)
                    break
            if i == n-1:
                result.append(0)
        return result
        """
    
            # Optimized Approach
        
        # Result array
        result = [0]*len(temperatures)
        # Reference stack to track 
        stack = []
        # Enumerate so we have index, value
        for index, value in enumerate(temperatures):
            # Iterate the stack when higher temperature is hit
            while stack and temperatures[stack[-1]] < value:
                select = stack.pop()
                result[select] = index - select
            stack.append(index)
        return result
            
