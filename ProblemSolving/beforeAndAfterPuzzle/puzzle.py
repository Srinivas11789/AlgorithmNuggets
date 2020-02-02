class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        
        # Naive O(N**2) iteration - 100 pass 6% faster
        
        # we use list instead of set() here to properly sort lexicographically
        result = []
        visited = set()
        
        # O(n**2) iteration
        for i in range(len(phrases)):
            for j in range(len(phrases)):
                if i != j:
                    p1 = phrases[i].split(" ")
                    p2 = phrases[j].split(" ")
                    #print(p1, p2)
                    if p1[-1] == p2[0]:
                        if " ".join(p1 + p2[1:]) not in visited:
                            visited.add(" ".join(p1 + p2[1:]))
                            result.append(" ".join(p1 + p2[1:]))
                    elif p1[0] == p2[-1]:
                        if " ".join(p2 + p1[1:]) not in visited:
                            visited.add(" ".join(p2 + p1[1:]))
                            result.append(" ".join(p2 + p1[1:]))
                    else:
                        continue
                    
        return sorted(result)
