class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Logic: Dynamic Programming - 100 100
        
        # References:
        # * https://leetcode.com/problems/unique-binary-search-trees/discuss/232795/python-easy-DP-beats-98
        # * https://leetcode.com/problems/unique-binary-search-trees/discuss/236389/6-lines-python-DP-solution-beats-100-python3-solutions
        
        # Subproblems for each number of nodes to n
        record = [0]*(n+1)
        
        # Empty node condition
        record[0] = 1
        # One node condition
        record[1] = 1
        
        # iterate for n from 2 to n
        for i in range(2, n+1):
            # All the previous subproblems are dependant, a choice made previous affects choice as we proceed --> so 1 to i
            for j in range(i):
                # Update record with the combinations that could occur for a given previous choice == value at j * future values until i
                record[i] += record[j] * record[i-j-1]
        return record[n]
                
