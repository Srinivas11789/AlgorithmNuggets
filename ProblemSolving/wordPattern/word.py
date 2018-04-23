class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        # Find the type of pattern first 
        
        # Initially create a mark of the pattern in a dictionary
        pattern = list(pattern)
        p = {}
        for i in range(len(pattern)):
            if pattern[i] not in p:
                p[pattern[i]] = []
            p[pattern[i]].append(i)
        print p
        
        # Separate the string and check for the pattern match
        string = string.split(" ")
        print string
        
        if not string or not pattern:
            return False
        
        prev = "str"
        check = None
        for k,v in p.items():
            count = 0
            check = None
            for val in v:
                if val < len(string):
                    if not check:
                        check = string[val]
                    if check == string[val]:
                        count += 1
            if check == prev:
                return False
            prev = check
            if count == len(v) and len(v) == string.count(check):
                pass
            else:
                return False
        return True
                
                    
                
            
            
        
