class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        # Logic1: does not work 
        # * Going greedy with min costs all along? - Doesnt work?
        # * iteration and logic below doesnt work
        """
        total = 0
        A = len(costs)//2
        B = len(costs)//2
        for c in costs:
            if A and c[0] < c[1]:
                total += c[0]
                A -= 1
            elif B and c[1] < c[0]:
                total += c[1]
                B -= 1
            else:
                if A:
                    total += c[0]
                    A -= 1
                elif B:
                    total += c[1]
                    B -=1
        return total
        """
        
        # Logic 2: Arrange and then perform - does not work
        """
        cityA = sorted(costs, key=lambda x: x[0])
        A = len(costs)//2
        total = 0
        while A:
            total += cityA.pop(0)[0]
            A -= 1
        B = len(costs)//2
        while B:
            total += cityA.pop(0)[1]
            B -= 1
        return total
        """
        
        # Logic 3: Find Delta and arrange them accordingly - 100 pass
        costs = sorted(costs, key=lambda x: x[0]-x[1])
        mid = len(costs)//2
        return sum(c[0] for c in costs[:mid])+sum(c[1] for c in costs[mid:])
