class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        last_seen_1 = None
        last_seen_2 = None
        
        mini = len(wordsDict)
        
        for i in range(len(wordsDict)):
            
            if wordsDict[i] == word1:
                last_seen_1 = i
                
            if wordsDict[i] == word2:
                last_seen_2 = i
            
            if last_seen_1 != None and last_seen_2 != None:
                if abs(last_seen_1-last_seen_2) < mini:
                    mini = abs(last_seen_1-last_seen_2)
        
        return mini
                
