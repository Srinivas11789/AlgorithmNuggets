class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        # logic 1: backtrack all choices for reaching the destination --> all basic passed except for time limit exceeded on scale test case
        """"
        stations.sort(key=lambda x: x[0])
        
        def backtrack(fuel, pos, last_stop, stations_visited):
            
            #print(fuel, pos, last_stop, stations_visited)
            
            if pos >= target or pos+fuel >= target:
                if len(stations_visited) < self.min_stops:
                    self.min_stops = len(stations_visited)
                return
            
            for s in range(last_stop, len(stations)):
                fuel_pos, new_fuel = stations[s]
                if pos+fuel >= fuel_pos:
                    # greedy if s+1 < len(stations) and pos+fuel < stations[s+1][0]:
                     backtrack(fuel-(fuel_pos-pos)+new_fuel, fuel_pos, s+1, stations_visited+[fuel_pos])
                else:
                    break
            
            return 
        
        self.min_stops = float('inf')
        backtrack(startFuel, 0, 0, [])
        if self.min_stops == float('inf'):
            return -1
        return self.min_stops
        """
        
        # 2 --> Dynamic Programming (sol ref) --> maximize the fuel at every stations
        
        dp = [startFuel] + [0]*len(stations)
        
        for i in range(len(stations)):
            loc, fuel = stations[i]
            for j in range(i,-1,-1):
                if loc > dp[j]:
                    continue
                dp[j+1] = max(dp[j+1], dp[j]+fuel)
               
        #print(dp)
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
            
        return -1
