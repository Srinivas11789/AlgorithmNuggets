class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # Logic 1: 100 pass 80% faster - Instead of using collections for each word lets use sorted of each word and use them as key for dictionarys
        anagrams = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        result = []
        for key, value in anagrams.items():
            result.append(value)
        return result
            
