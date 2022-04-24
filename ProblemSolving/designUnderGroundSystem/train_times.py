class UndergroundSystem:

    def __init__(self):
        
        self.trip_times = {} 
        self.customer_onboarded = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
         
        if id not in self.customer_onboarded:
            self.customer_onboarded[id] = []
            
        self.customer_onboarded[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        startPoint, startTime = self.customer_onboarded[id]
        totalDuration = t - startTime
        key = startPoint + "->" + stationName
        
        if key not in self.trip_times:
            self.trip_times[key] = [0, 0]
        
        self.trip_times[key][0] += totalDuration
        self.trip_times[key][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        key = startStation + "->" + endStation
        
        # there is always a trip so we dont need to check key existence, it shld always be true
        if key not in self.trip_times:
            return False
        
        return self.trip_times[key][0]/self.trip_times[key][1]
            

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
