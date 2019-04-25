class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        # First, Sort days based on their delta or difference between cityA and cityB
        sorted_differences = sorted(costs, key=lambda x: x[0] - x[1])
        
        # N for each city, given array is 2N
        N = len(costs)//2
        min_cost = 0
        
        # Second, for the first few differences use cityA's value, because the lower differences means x[0] in minimum in x[0]-x[1]
        min_cost += sum(i[0] for i in sorted_differences[:N])
        
        # Third, for rest of the days use cityB
        min_cost += sum(i[1] for i in sorted_differences[N:])
        
        return min_cost
    
        # This logic below doesnot work for [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], which makes me think the difference or delta is more important here
        """
        # Count for city A and B each
        cityA = 0
        cityB = 0
        
        # As 2N people are already given.
        N = len(costs)//2
        
        min_cost = 0
        
        for candidate in costs:
            if candidate[0] < candidate[1] and cityA < N:
                min_cost += candidate[0]
                cityA += 1
            elif cityB >= N:
                min_cost += candidate[0]
                cityA += 1
            else:
                min_cost += candidate[1]
                cityB += 1
            # Just this wont work as we need to have N in each city
            ## min_cost += min(candidate[0], candidate[1])
            print min_cost, cityA, cityB
        return min_cost
        """
        
        
