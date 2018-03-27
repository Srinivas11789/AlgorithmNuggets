# Scope Problem 
class Difference:
	# Add your code here
    def __init__(self,a):
        self.numlist = sorted(a)
        
    def computeDifference(self):
        self.maximumDifference = self.numlist[len(self.numlist)-1]-self.numlist[0]
        return
        

# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
