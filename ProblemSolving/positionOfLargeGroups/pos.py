class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        
        n = len(S)
        select = None
        count = 0
        result = []
        i = 0
        while i < n:
            if select == None:
                select = i
                count += 1
                i += 1
            else:
                if S[i] == S[select]:
                    count += 1
                    i += 1
                else:
                    #print S[select], count
                    if count >= 3:
                        result.append([select, i-1])
                    select = None
                    count = 0
        if count >= 3:
            result.append([select, i-1])
        return result
            
