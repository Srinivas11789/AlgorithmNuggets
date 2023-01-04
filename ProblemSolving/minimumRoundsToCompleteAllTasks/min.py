class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        # 1. Memoize the difficulty levels and find maximum difficulty
        difficulty = {}
        round = 0
        for t in range(len(tasks)):
            if tasks[t] not in difficulty:
                difficulty[tasks[t]] = 1
                continue
            difficulty[tasks[t]] += 1

        # 2. DP: Calc mins of all difficulty upto max difficulty
        difficulty_memo = {
            0: 0,
            1: float('inf'),
            2: 1,
            3: 1
        }
        def recurse_min(n):
            if n in difficulty_memo:
                return difficulty_memo[n]
            difficulty_memo[n] = 1 + min(recurse_min(n-2), recurse_min(n-3))
            return difficulty_memo[n]

        for k,v in difficulty.items():
            min_rounds = recurse_min(v)
            if min_rounds == float('inf'):
                return -1
            round += min_rounds
            print(difficulty_memo, k, v, round)

        return round
