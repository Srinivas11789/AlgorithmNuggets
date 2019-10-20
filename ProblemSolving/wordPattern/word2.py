class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        # Logic 1:
        # We loose the positions of the characters in string.. so this wont work
        #return len(set(pattern)) == len(set(str.split(" ")))
        
        # Logic 2:
        relation = {}
        visited = set()
        s = str.split(" ")
        if len(s) != len(pattern):
            return False
        for i, j in zip(pattern, s):
            if i not in relation and j not in visited:
                relation[i] = j
                visited.add(j)
            if i in relation and relation[i] == j:
                pass
            else:
                return False
        return True
