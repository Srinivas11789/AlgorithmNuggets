class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        result = []
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0]
            local_name = "".join(local_name.split("."))
            result_email = local_name+"@"+domain_name
            if result_email not in result:
                result.append(result_email)
        return len(result)
