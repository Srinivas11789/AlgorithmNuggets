class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        
        # Logic 1: Literally following the problem description - 100 pass 75% faster
        
        # Split date into corresponding year, month, day
        year, month, day = date.split("-")
        
        # Days of the month
        days_in_a_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Leap year check
        if int(year)%400 == 0 or (int(year)%4 == 0 and int(year)%100 != 0):
            days_in_a_month[1] = 29
        
        # No of days just within a year is calculating month (month days until that resp month) and days
        num = sum(days_in_a_month[:int(month)-1])+int(day)
        return num
            
            
