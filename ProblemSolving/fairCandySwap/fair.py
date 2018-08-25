class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        # Find the diff of the sums (divide by 2 to calculate the weight on B) and then check for b+diff in A, As the problem says there should always be an answer, an entry would surely exist in b which matches A
        a, b, diff = set(A), set(B), (sum(A) - sum(B))/2
        for b in B:
            if b + diff in a:
                return [b+diff, b]
            
