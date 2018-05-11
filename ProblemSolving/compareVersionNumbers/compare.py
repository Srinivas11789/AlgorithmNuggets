### Lesson learnt
* Dont club all the types of logic into one solution, using int or stripping would have worked right away, but included both and wasted time even when the logic was correct
* 0000 to int will give only 0 so problem solved --> int("0000") = 0

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        n = len(version1)
        m = len(version2)
        
        answer = 0
       
        # Padding 
        if m-n > 0:
            version1.extend(list("0"*(m-n)))
        elif n-m > 0:
            version2.extend(list("0"*(n-m)))
        
        for v1,v2 in zip(version1,version2):
            """
            if len(v1) > 1:
                v1 = v1.lstrip("0")#.rstrip("0")
            if len(v2) > 1:
                v2 = v2.lstrip("0")#.rstrip("0")
            #print v1,v2
            """
            if int(v1) > int(v2):
                return 1
            elif int(v2) > int(v1):
                return -1
        return 0
                

