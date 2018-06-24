# Pending...

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        
        def timeDelta(time1, time2):
            h1,m1 = time1.split(":")
            h2,m2 = time2.split(":")
            """
            if h1 == "00":
                h1 = 24
            if h2 == "00":
                h2 = 24
            if m1 == "00":
                m1 = 60
            if m2 == "00":
                m2 = 60
            #t1 = int(h1)*60+int(m1)
            #t2 = int(h2)*60+int(m2)
            print t1, t2
            """
            return (int(h2)-int(h1))*60+(int(m2)-int(m1))
            
            """
            # Not a proper logic for time delta
            if min1 == "00":
                min1 = 24
            if min2 == "00":
                min2 = 24
            if sec1 == "00":
                sec1 = 60
                min1 = int(min1)-1
            if sec2 == "00":
                sec2 = 60
                min2 = int(min2)-1
            #mindiff = abs(int(min1)-int(min2))
            #secdiff = abs(int(sec1)-int(sec2))
            #result = float(str(mindiff)+"."+str(secdiff))
            #return abs(int(sec1)-int(sec2))
            result = abs(float(str(min1)+"."+str(sec1))-float(str(min2)+"."+str(sec2)))
            result_min = int(str(result).split(".")[0])*60
            result_sec = int(str(result).split(".")[1])
            print result_min,result_sec
            return result_min+result_sec
            """
        
        mini = float('inf')
        for i in range(len(timePoints)):
            for j in range(len(timePoints)):
                if i != j:
                    if timeDelta(timePoints[i],timePoints[j]) < mini:
                        mini = timeDelta(timePoints[i],timePoints[j])
        return mini
