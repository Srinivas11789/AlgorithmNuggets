class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        
        s = sentence.split(" ")
        for item in dict:
            for i in range(len(s)):
                n = len(item)
                if item == s[i][:n]:
                    s[i] = item
        return " ".join(s)
                    
        
        
        
