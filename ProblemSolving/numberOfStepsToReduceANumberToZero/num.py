class Solution:
    
    # Logic 1: Iterative --> Literally following the description - 100 pass
    """
    def numberOfSteps (self, num: int) -> int:
        step = 0
        while num:
            if num%2 == 0:
                num = num//2
            else:
                num -= 1
            step += 1
        return step
    """
    
    # Logic 2: Recursive --> same as above - 100 pass
    def numberOfSteps (self, num: int) -> int:
        
        def reduce(num: int, steps: int):
            # Exit criteria
            if num == 0:
                return steps
            
            # Reduce to subproblems
            if num%2 != 0:
                num -= 1
            else:
                num = num//2
            
            # Recurse each sub problem
            return reduce(num, steps+1)
        
        return reduce(num, 0)
            