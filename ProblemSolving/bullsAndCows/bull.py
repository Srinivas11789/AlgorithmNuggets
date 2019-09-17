class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        # Logic n: 100 pass

        # Bull Count
        A = 0
        # Cow Count
        B = 0
        
        #One iteration to find out the equal index
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                A += 1
        # OR
        #A = sum([i==j for i,j in zip(secret, guess)])
                
        # Two all other intersections
        #print(collections.Counter(secret), collections.Counter(guess), (collections.Counter(secret) & collections.Counter(guess)))
        B = sum((collections.Counter(secret) & collections.Counter(guess)).values())-A
        
        
        # In search of optimization to O(N)
        
        # Logic 1: Naive Iteration - Fail!
        """
        visited = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                if guess[i] in visited:
                    B -= 1
                A += 1
            elif guess[i] in secret[:i]+secret[i+1:]:
                if guess[i] not in visited:
                    visited.append(guess[i])
                    B += 1
            print(visited, A, B)
        
        i = 0
        secret = list(secret)
        guess = list(guess)
        while i < len(secret):
            if secret and guess and secret[i] == guess[i]:
                A += 1
                secret.pop(i)
                guess.pop(i)
            else:
                
                i += 1
        """
        """
        C1 = collections.Counter(secret)
        C2 = collections.Counter(guess)
        print(C1,C2)
        """
            
        # Logic 2: Use extra space a dictionary -> wont work for duplicates - Fail!
        """
        import collections
        counts = collections.Counter(secret+guess)
        for k,v in counts.items():
            if v == 2 and k in secret and k in guess and secret.index(k) == guess.index(k):
                A += 1
            else:
                B += 1
        """
        
        return str(A)+"A"+str(B)+"B"
        
