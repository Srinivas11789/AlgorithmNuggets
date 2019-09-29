        # O(N) over the string with the character counts
        # * We want at most one occurrence of any character, which means we need the character occuring in only one of the word
        
        import collections
        counts = collections.Counter(S)
        visited = []
        result = []
        start = 0
        for i in range(len(S)):
            counts[S[i]] -= 1
            if counts[S[i]] == 0:
                visited.append(S[i])
            print(set(visited), set(S[start:i+1]), S[start:i+1])
            if visited and set(S[start:i+1]) == set(visited):
                result.append(len(S[start:i+1]))
                visited = []
                start = i+1
        return result
