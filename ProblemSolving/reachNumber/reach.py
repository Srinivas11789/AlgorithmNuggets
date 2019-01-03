class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        """
        # Logic 1: Own greedy approach (pending... not complete) 
        # This does not give minimum number of steps...
        
        # target == 0 condition
        if target == 0:
            return 0
        
        # Initial starting point set to 0
        start = 0
        
        # This can go 2 ways 
        # * At every step or number, we could go -n or +n and further like that (it tapers down as a tree and the best path (min) should be selected.)
        # --> Greedy or Dynamic Prog?
        # Let's do greedy
        # * Every time we move towards the targets which would be the closest to the target
        # * We avoid the steps which would make use greater than target
        step = 0
        target = abs(target)
        while start != target:
                step += 1
                if start+step > target:
                    start -= step
                else:
                    start += step
                print start, step
        return step
        """
        
        
        # 100 pass - 100 ms runtime 19.02 faster
        # Mathematical solution
        # Based on https://leetcode.com/problems/reach-a-number/discuss/112968/Short-JAVA-Solution-with-Explanation
        
        # Always move towards the target (Right)
        # * If the sum exceeds target
        #   - Exceed until the difference is even (this makes sure there can be some left motions to succeed)
        
        step = 0
        start = 0
        
        # Number line is identical on both sides. Lets consider one side always and calculate the result
        
        target = abs(target)
        
        # Move right side until target is equaled or just exceeded
        while start < target:
            step += 1
            start += step
            
        while (start - target) % 2 != 0:
            step += 1
            start += step
        
        return step
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
