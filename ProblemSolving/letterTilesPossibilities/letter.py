class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        
        def backtrack(labels, path, res):
            if path and path not in res:
                res.add(path)
            for i in range(len(labels)):
                backtrack(labels[:i]+labels[i+1:], path+labels[i], res)
            
        result = set()
        backtrack(tiles, "", result)
        return len(result)
