import copy

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        cache = {}
        for i in range(len(tiles)):
            t = tiles[i]
            if t not in cache:
                cache[t] = 0
            cache[t] += 1

        # single 
        self.n = len(cache)

        def backtrack(comb, exists, remaining):
            if len(comb) > 1 and comb not in exists:
                exists.add(comb)
                #print(exists)
                self.n += 1
            for k, v in remaining.items():
                if v == 0:
                    continue
                newr = copy.deepcopy(remaining)
                newr[k] -= 1
                backtrack(comb+k, exists, newr)

        backtrack("", set(), cache)
        return self.n
