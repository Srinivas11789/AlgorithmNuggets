class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        
        # Logic 2: Do not go over the range og flight bookings, Instead
        # * Increment seats at the start of the range say i
        # * Decrement these seats at after j as we need to reduce them (j+1)
        # Idea from https://leetcode.com/problems/corporate-flight-bookings/discuss/328856/JavaC%2B%2BPython-Straight-Forward-Solution
        
        # Hold all the flight bookings
        flights = [0]*(n+1)
        # Iterate booking
        for booking in bookings:
            # At the range start, Increment num of seats
            flights[booking[0]-1] += booking[2]
            # Remove thos seats at j+1
            flights[booking[1]] -= booking[2]
        # Correct the range with one iteration
        # * Add previous to the current booking
        for i in range(1, n):
            flights[i] += flights[i-1]
        return flights[:-1]
            
        
        # Logic 1: Naive method of Iteration - 99 pass ( time limit exceeded on the scale test case)
        """
        flights = [0]*(n+1)
        for booking in bookings:
            for flight in range(booking[0], booking[1]+1):
                flights[flight] += booking[2]
        return flights[1:]
        """
