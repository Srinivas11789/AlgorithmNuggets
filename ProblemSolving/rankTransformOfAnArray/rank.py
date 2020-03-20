class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        
        # Logic 1: O(N) using dictionary to store sorted indexes - 100 pass - 70% faster
        
        # Sort to get ranks
        ranks = sorted(arr)

        # Create dict and add indexes, handle duplicates!
        indexes = {}
        prev = 0
        for i in range(len(ranks)):
            if ranks[i] not in indexes:
                prev += 1
                indexes[ranks[i]] = prev
            else:
                pass
        
        # Final iteration to replace with ranks
        for i in range(len(arr)):
            arr[i] = indexes[arr[i]]
        return arr
            
            
        # Logic 2: Hacky Way - Works for few cases but eventually time limit exceeded for scale cases
        """
        ranks = set(arr)
        return map(lambda x: ranks.index(x)+1, arr)
        """
