class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        
        # Logic 1: All combinations brute force - Obviously time limit exceeded! Otherwise all test cases passed
        """
        dice = [range(1,f+1) for i in range(d)]
        #print(dice)
        import itertools
        times = 0
        n = len(dice)-1
        if n <= 0:
            n = 1
        for comb in itertools.product(*dice, repeat=n):
            #print(comb)
            if sum(comb) == target:
                times += 1
        return times
        """
        
        # Logic 2: We can leverage the sum logic here, once we select one dice value all other dice values are target-selected value
        # * also all the subproblems ( each dice roll ) affects the next dice roll's choice - dynamic programming like
        # * Lets go recursive with top down approach
        # * Time Limit exceeded with 30, 30 , 500 --> We need to memoize or cache values
        """
        def roll(next_dice, targt):
            print(next_dice, targt)
            if next_dice <= d:
                for face in dice.keys():
                    next_face = targt - face
                    print(face, next_face)
                    if next_dice == d and next_face == 0:
                        self.times += 1
                        return
                    elif next_face > 0:
                        roll(next_dice+1, next_face)
            else:
                return 
        
        import collections
        dice = collections.Counter(range(1,f+1))
        self.times = 0
        roll(1, target)
        return self.times
        """
        
        # Logic 3: DP with Table for reference
        dp = [[0 for i in range(target+1)] for j in range(d+1)]
        dp[0][0] = 1
        mod = 10**9 + 7
        for i in range(1,d+1):
            for j in range(1,target+1):
                k = 1
                while k <= min(j,f):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % mod
                    k += 1
        return dp[d][target] % mod
