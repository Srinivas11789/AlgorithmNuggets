class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def buildIPs(remaining, current, subnets):
            
            if not remaining and current and subnets == 4:
                self.ips.append(current[1:])
            
            if remaining and subnets != 4:
                for i in range(3):
                    #print(i, remaining, current, subnets)
                    if i == 0:
                        buildIPs(remaining[:-1], "." + remaining[-1:] + current, subnets +1 )
                    if i == 1 and len(remaining) > 1 and remaining[-2] != "0":
                        buildIPs(remaining[:-2], "." + remaining[-2:] + current, subnets +1 )
                    if i == 2 and len(remaining) > 2 and remaining[-3] in {"1","2"} and int(remaining[-3:]) <= 255:
                        buildIPs(remaining[:-3], "." + remaining[-3:] + current, subnets +1 )
        
        self.ips = []
        buildIPs(s, "", 0)
        return self.ips
            
        
