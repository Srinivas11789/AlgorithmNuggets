class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        ### Logic 2: 55% faster
        # * take the good parts of logic 1
        # * Perform something similar to BFS in BST
        # * good ref: https://leetcode.com/problems/synonymous-sentences/discuss/430604/Java-BFS-Solution-Picture-Explain-Clean-code, https://leetcode.com/problems/synonymous-sentences/discuss/729580/JavaScript-BFS-undirected-graph-lightly-commented        
 
        # 1. create graph
        g = {}
        
        for s in synonyms:
            if s[0] not in g:
                g[s[0]] = []
            if s[1] not in g:
                g[s[1]] = []
            g[s[0]].append(s[1])
            g[s[1]].append(s[0])
        
        # 2. Maintain a list of possible candidates as stack to traverse/iterate
        stack = [text]
        visited = set()
        
        # 3. Iterate over the stack
        while stack:
            # Update current and visited
            current = stack.pop(0)
            if current not in visited:
                visited.add(current)
            # Placeholders and replace
            words = current.split(" ")
            for w in range(len(words)):
                if words[w] in g:
                    for v in g[words[w]]:
                        words[w] = v
                        candidate = " ".join(words)
                        if candidate not in visited:
                            visited.add(candidate)
                            stack.append(candidate)
        return sorted(visited)
        
        
        ### Logic 1: Computational intensive and does not work with some cases...
        # * Create a graph
        # * Get all synonyms
        # * Create placeholders in text
        # * Backtrack all combinations and fill in
        """
        words_that_mean_the_same = []
        g = {}
        visited = set()
        words = text.split(" ")
        uniq = set(words)
        fmt = set()
        fmts = []
        
        # 1. Get all the possible values for each position in a array
        
        # Graph traverse or expand relation into one path
        def traverse_graph(node):
            words_that_mean_the_same[-1].append(node)
            if node in g and node not in visited:
                visited.add(node)
                traverse_graph(g[node])
        
        for n in synonyms:
            if n[0] not in g:
                g[n[0]] = n[1]
            else:
                print("duplicate key")
        
        for n in g:
            if n not in visited:
                visited.add(n)
                words_that_mean_the_same.append([n])
                traverse_graph(g[n])
                cfmt = uniq.intersection(words_that_mean_the_same[-1])
                fmt.update(cfmt)
                fmts.append(cfmt)
                if len(cfmt) == 0:
                    words_that_mean_the_same.pop()
                else:
                    words_that_mean_the_same[-1].sort()
        
        # 2. Placeholders
        start = 65
        hold = []
        for w in range(len(words)):
            if words[w] in fmt:
                for i in range(len(fmts)):
                    if words[w] in fmts[i]:
                        words[w] = chr(start+i)+chr(start+i)
                        hold.append(chr(start+i)+chr(start+i))
                        
        hold = list(set(hold))
        
        # 3. Fill in
        result = []
        fmtStr = " ".join(words) 
        n = len(words_that_mean_the_same)
        def backtrack(i, curr):
            if i == n:
                print(fmtStr, curr, words_that_mean_the_same, fmt, hold)
                #result.append(fmtStr % curr*len())
                for h in range(len(hold)):
                    fmtStr.replace(hold[h], curr[h])
            else:
                for w in words_that_mean_the_same[i]:
                    backtrack(i+1, curr + (w,))

        backtrack(0, ())
        return result
        """
                
        
         
            
