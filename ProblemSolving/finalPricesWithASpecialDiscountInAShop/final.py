class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Logic 1: Obvious almost NM**2 of running until last index at each index considered - 100 pass 53% faster
        """
        for i in range(len(prices)):
            mini = prices[i+1:]
            for j in range(len(mini)):
                if mini[j] <= prices[i]:
                    prices[i] -= mini[j]
                    break
        return prices
        """
        # Logic 2: Having a convergence stage of making relationship before iterating
        # * Keep a record of the sorted array
        # * index to element relation in a dictionary
        # * Convergence can again take almost equal complexity
        
        # Logic 3: Using inbuilt min function at every index --> the first min index is asked so this effort is not worth
        
        # Logic 4: O(N) Using a separate stack or array to feed all the greater ones so when we hit the first min <= element we can apply the condition 
        # * Ref: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/discuss/685390/JavaC%2B%2BPython-Stack-One-Pass
        stack = [] # Separate stack to store element that still need to be computed for discount
        for i in range(len(prices)):
            #print(stack)
            while stack and prices[stack[-1]] >= prices[i]: # current element is first min index >= the stack element
                prices[stack.pop()] -= prices[i] # Apply discount
            stack.append(i) # Add to stack to compute this later in iteration
        return prices
        

