class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
       	
	""" 
        if s.count("A") > 1:
            return  False
        
        count = 1
        for i in range(len(s)-1):
            if s[i] == "L" and s[i] == s[i+1]:
                count += 1
            else:
                count = 1
            if count > 2:
                return False
            
        return True
        """

        # Logic 1: O(N) naive iteration to go over the attendance
        Absent = 0
        Late = 0
        for i in range(len(s)):
            
            # Update Values
            if s[i] == "A":
                Absent += 1
                Late = 0
            elif s[i] == "L":
                Late += 1
            else:
                Late = 0
            
            # Check Conditions
            if Absent > 1:
                return False
            elif Late > 2:
                return False
            
        return True
        
