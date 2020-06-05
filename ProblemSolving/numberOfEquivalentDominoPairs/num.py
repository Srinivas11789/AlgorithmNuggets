class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        
        # Logic 2: Use SET/Dictionary of all the pairs as string and check if we have already visited O(N) space O(N) - 95% faster
        pairs = {}
        count = 0
        for domino in dominoes:
            if domino[0] < domino[1]:
                key = domino[0]*10 + domino[1]
            else:
                key = domino[1]*10 + domino[0]
            if key in pairs:
                pairs[key] += 1
            if key not in pairs:
                pairs[key] = 0
        for key, value in pairs.items():
            if pairs[key] > 0:
                pairs[key] += 1
                count += (pairs[key]*(pairs[key]-1))//2
        return count
        
        # Logic 1: Naive O(N2) logic - Time Limit Exceeded
        """
        count = 0
        for d in range(len(dominoes)):
            for e in range(d+1, len(dominoes)):
                if dominoes[d] == dominoes[e] or dominoes[d] == dominoes[e][::-1]:
                    count += 1
        return count
        """
