class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        # Understanding
        # * Split by @ to get ==> localname and domain name
        # * "." => split by "." and join without it or replace "." by ""
        # * "+" => split by "+" and take index 0
        # * last 2 rule only applies to localname
        
        # Iteration over the list
        result = []
        for email in emails:
            
            # Identify names
            localname, domainname = email.split("@")
            
            # Rule 1 about "."
            if "." in localname:
                localname = localname.replace(".","")
            
            # Rule 2 about "+"
            if "+" in localname:
                localname = localname.split("+")[0]
                
            filtered_email = localname+"@"+domainname
            
            if filtered_email not in result:
                result.append(filtered_email)
        
        return len(result)
            
            
                
            
