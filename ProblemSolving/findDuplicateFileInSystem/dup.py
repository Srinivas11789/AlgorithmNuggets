class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        directory = {}
        
        for path in paths:
            current = path.split(" ")
            for file in current[1:]:
                content = file.split("(")
                if content[1][:-1] not in directory:
                    directory[content[1][:-1]] = []
                directory[content[1][:-1]].append(current[0]+"/"+content[0])
        
        result = []
        for k,v in directory.items():
            if len(v) >= 2:
                result.append(v)
        return result
            
                
    
            
