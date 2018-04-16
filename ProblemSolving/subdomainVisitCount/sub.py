class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        result = {}
        for domain in cpdomains:
            visits, full_domain = domain.split(" ")
            domains = full_domain.split(".")
            #for i in range(len(domains)):
            #    d = full_domain[full_domain.index(domains[i]):]
            i = 0
            while i < len(domains):
                d = ".".join(domains)
                if d not in result:
                    result[d] = int(visits)
                else:
                    result[d] += int(visits)
                del domains[i]
        #print result
        final = []
        for key, value in result.items():
            final.append(str(value)+" "+key)
        
        return final
            
