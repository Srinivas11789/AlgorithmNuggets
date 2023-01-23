class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trustGraph = {}

        for t in range(len(trust)):

            a = trust[t][0]
            b = trust[t][1]

            if a not in trustGraph:
                trustGraph[a] = set()
            if b not in trustGraph:
                trustGraph[b] = set()

            trustGraph[a].add(b)

        possibleJudges = []
        for k,v in trustGraph.items():
            if len(v) == 0:
                possibleJudges.append(k)
        
        if len(trust) == 0 and n == 1:
            return 1
