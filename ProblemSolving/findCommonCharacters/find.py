class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        
        # Logic:
        # 1. Using set ==> we might loose the duplicate common elements 
        # 2. Using counter() ==> intersection depends on the prefix counter
        # 3. bruteforce or naive method
        
        result = list(A[0])
        
        for word in A[1:]:
            i = 0
            word = list(word)
            while i < len(result):
                if result[i] not in word:
                    del result[i]
                else:
                    del word[word.index(result[i])]
                    i += 1
        return result
                    
                    
                    
        
                
