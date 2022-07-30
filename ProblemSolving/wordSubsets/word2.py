class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        universal = []
        
        # All subsets combined together
        subsets = {}
        for w in words2:
            curr = {}
            for c in w:
                if c not in curr:
                    curr[c] = 0
                curr[c] += 1
            for k, v in curr.items():
                if k not in subsets:
                    subsets[k] = v
                    continue
                subsets[k] = max(subsets[k], v)
        
        # Iterate to check for universal
        for word in words1:
            ref = {}
            for i in range(len(word)):
                if word[i] not in ref:
                    ref[word[i]] = 0
                ref[word[i]] += 1
                
            isASubset = True
            matched = 0
            for k,v in ref.items():
                if k not in subsets:
                    continue
                if subsets[k] > v:
                    isASubset = False
                    break
                matched += 1
            
            print(matched, isASubset, ref, subsets)
            if isASubset and matched == len(subsets):
                universal.append(word)
                
        return universal
        
        
        """
        # checking one by one wont help. We shld combine the subsets
        
        universal = []
        
        for word in words1:
            ref = {}
            for i in range(len(word)):
                if word[i] not in ref:
                    ref[word[i]] = 0
                ref[word[i]] += 1
            subset = True
            counts = 0
            for word2 in words2:
                if not subset:
                    break
                r  = ref.copy()
                count =0
                for ch in word2:
                    if ch not in r:
                        break
                    if r[ch] == 0:
                        break
                    r[ch] -= 1
                    count += 1
                if count == len(word2):
                    subset = True
                    counts += 1
                else:
                    subset = False
            if counts == len(words2):
                universal.append(word)
                
        return universal
        """
