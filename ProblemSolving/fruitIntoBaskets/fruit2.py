class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        max_fruits = 0
        for start in range(len(tree)):
            types = {tree[start]}
            start_max = 0
            while tree[start] > 0:
                if tree[start] not in types and len(types) < 2:
                    types.add(tree[start])
                    
                # Return if more than tree types
                if len(types) == 2 and tree[start] not in types:
                    break
                    
                # Break if no fruit else add
                if tree[start] > 0:
                    start_max += 1
                    tree[start] -= 1
                else:
                    break
                
                # Rotate and continue if condition satisfies
                if start+1 < len(tree) and tree[start+1] > 0:
                    start = start + 1
                elif start + 1 == len(tree) and tree[0] > 0:
                    start = 0
            if start_max > max_fruits:
                max_fruits = start_max
        return max_fruits
