class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        
        import collections
        universal = []
        sort = [0]*len(B)
        
        for word in A:
            count = 0
            superset = collections.Counter(word)
            for subset in range(len(B)):
                if sort[subset] == 0:
                    B[subset] = collections.Counter(B[subset])
                    sort[subset] = 1
                intersection = list((B[subset] & superset).elements())
                #print intersection, B[subset], superset
                if len(intersection) == sum(B[subset].values()) :
                    count += 1
            #print count
            if count == len(B):
                universal.append(word)
        return universal
        
        
        """
        # Logic: Subset with sorted ( Doesnt work when high delta sep characters are present )
        universal = []
        sort = [0]*len(B)
        
        for word in A:
            count = 0
            superset = "".join(sorted(word))
            for subset in range(len(B)):
                if sort[subset] == 0:
                    B[subset] = "".join(sorted(B[subset]))
                    sort[subset] = 1
                print B[subset], superset
                if B[subset] in superset:
                    count += 1
            print count
            if count == len(B):
                universal.append(word)
        return universal
        """
        
