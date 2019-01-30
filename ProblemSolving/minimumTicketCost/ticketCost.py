class Solution(object):
    def mincostTickets(self, days, cost):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        # Logic 1: Solving with Dynamic Programming 
        # This logic as inreference to the discuss thread - https://leetcode.com/problems/minimum-cost-for-tickets/discuss/228421/Python-solution
        
        # Create dictionary for faster lookup of days
        import collections
        days_dict = collections.Counter(days)
        
        # Create a table of all the day cost
        # * Instead of creating a 365 days table, we create until the last day on the days list
        table = [0 for i in range(0, days[-1]+1)]
        
        for i in range(0, days[-1]+1):
            # If the current day is not present in the travel days dictionary, it takes the previous value
            if i not in days_dict:
                table[i] = table[i-1]
            else:
                # Used max to identify if the index exists 
                table[i] = min(
                    table[max(0,i-1)]+cost[0], # per days value
                    table[max(0,i-7)]+cost[1], # per week value
                    table[max(0,i-30)]+cost[2] # per year value
                )
       
        return table[-1]
        
        """
        # Logic 2: Solving without Dynamic Programming literally going over the logic definition mathmatically
        # * fails in some scenarios where the minimum cost could be achieved in a more different way
        
        # Days of travel
        # Costs - {per day, per 7 days, per month}

        n = len(days)
        i = 0

        import math
        # How much individual days cost to a week's pass
        per_day_cost_week = cost[1]//7 # (days)
        minimum_days_benefit_week_pass = cost[1]//cost[0] #(days)
        # How much individual week cost to a year's pass
        per_day_cost_year = cost[2]//365 # (days)
        minimum_days_benefit_month_pass = cost[2]//cost[0] #(days)

        total_cost = 0
        print minimum_days_benefit_week_pass, minimum_days_benefit_month_pass 

        while i < n :
            # Each day
            # * Check yearly cost
            # * Check weekly pass benefit
            week_days_from_current_day = days[i]+7
            week_count = 0
            j = i
            while j < n and days[j] < week_days_from_current_day:
                week_count += 1
                j += 1
            month_days_from_current_day = days[i]+30
            month_count = week_count
            k = j
            while k < n and days[k] < month_days_from_current_day:
                month_count += 1
                k += 1
            if week_count > minimum_days_benefit_week_pass:
                # Single week cost will be a benefit!
                total_cost += cost[1]
                i = j
            elif month_count >  minimum_days_benefit_month_pass:
                total_cost += cost[2]
                i = k
            else:
                # Single day cost will only be a benefit!
                total_cost += cost[0]
                i += 1
            print total_cost, week_count, month_count
        return total_cost
        """