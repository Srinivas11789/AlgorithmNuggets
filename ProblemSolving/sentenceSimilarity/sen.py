class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        
        # Logic 1: Create relationship pairs and compare - 81% faster
        
        # Rule3: Same Length Words
        if len(words1) != len(words2):
            return False
        
        # Contruct relationship
        pair = {}
        for p in pairs:
            if p[0] not in pair:
                pair[p[0]] = set()
            pair[p[0]].add(p[1])
            if p[1] not in pair:
                pair[p[1]] = set()
            pair[p[1]].add(p[0])

        # Rule1,2: Iterate for Similarity
        for p in range(len(words1)):
            if not pair and words1[p] == words2[p]:
                continue
            elif (words1[p] in pair and words2[p] in pair[words1[p]]) or (words2[p] in pair and words1[p] in pair[words2[p]]):
                continue
            elif words1[p] == words2[p]:
                continue
            else:
                print(p, words1[p], words2[p])
                return False
        return True
