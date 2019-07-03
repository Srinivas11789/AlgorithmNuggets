class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool


        # Lesson:
        # The right mood and mindset would allow you to solve anything easily!
        # * Take rest and off sometime and get your mood for the problem
        # * one shot solve of a problem attempted earlier with a new logic

        # Logic: 100 pass: A slower logic but passes all scenarios. 
        # * Plot all the route and calculate capacity at each point, return false if it exceeds
        """
        #trips = [[2,1,5],[3,3,7]]
        #capacity = 4
        route = []
        for trip in trips:
            if len(route) < trip[2]:
                route.extend([0]*(trip[2]-len(route)))
            #print(route, trip[2])
            for road in range(trip[1], trip[2]):
                route[road-1] += trip[0]
                #print(route[road-1], capacity)
                if route[road-1] > capacity:
                    return False
        return True
        
        
        """
        # No 100 pass - an attempt to finish later
        # Logic 1: Fails (works only for iterative increase) Literally following through all the trips and calculating if capacity exceeds
        # * This logic works assuming the ranges (start->end) only overlap for the next trip and not further
        # * If there exist a trip farther in the list overlapping subset of the entire or initial part of the array then this fails
        
        # num of passengers: destination address
        
        start = []
        end = []
        passengers = []
        
        for trip in trips:
            print end, passengers, capacity, trip
            if end and trip[1] >= end[-1]:
                end.pop()
                start.pop()
                capacity += passengers.pop()
            elif end and trip[2] <= end[-1] and trip[1] > start[-1]:
                break
            elif start and trip[1] < start[-1]:
                return False
            passengers.append(trip[0])
            end.append(trip[2])
            start.append(trip[1])
            capacity -= trip[0]
            if capacity < 0:
                return False
        return True
        """
        
        """
        No 100 pass - an attempt to finish later!!
        # Logic 2: Overlapping subsets
        # * We need to solve this global for any overlapping range across the entire array
        
        # Method 1
        
        # sort by the start interval
        trips = sorted(trips, key=lambda x: x[1])
        
        
        end = []
        seats = []
        for trip in trips:
            
            # Overlapping subsets
            
            # Case1: When a subset falls within the previous subset
            # Case2: When a subset overlaps and exceeds the previous subset
            
            #if end and trip[2] <= end[-1]:
            #    capacity -= trip[1]
            #elif end and trip[1] < end[-1] and trip[2] > end[-1]:
            #    if seats[-1] + trip[0] > capacity:
            #        return False
            #    capacity += seats.pop()
            #    end.pop() 
            
            
            if trip[1] < end[-1]:
                capacity -= trip[0]
            else:
                capacity += 

            # For every trip add to the list and calculate capacity ( non overlapping )
            end.append(trip[2])
            seats.append(trip[1])
            
            # Fail if capacity is exceeded
            if capacity < 0:
                return False
        
        # True otherwise
        return True
        """
