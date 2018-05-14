class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 100 pass - Iteration
        magazine = list(magazine)
        for char in ransomNote:
            if char in magazine:
                #print char, magazine
                del magazine[magazine.index(char)]
            else:
                return False
        return True
        
        """
        # 100 pass - Dictionary method
        counts = {}
        for char in magazine:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        
        for char in set(ransomNote):
            if char not in counts.keys():
                return False
            if ransomNote.count(char) <= counts[char]:
                pass
            else:
                return False
        return True
        """
                
        
