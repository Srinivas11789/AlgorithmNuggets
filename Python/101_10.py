################### Stack and Queue Data Structure
import system
class Solution:
    # Stack Primitives
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def pushCharacter(self,item):
        self.stack.append(item)
        return
        
    def enqueueCharacter(self,item):
        n = len(self.queue)
        self.queue.append(item)
        return
        
    def popCharacter(self):
        item = self.stack[len(self.stack)-1]
        del self.stack[len(self.stack)-1]
        return item
    
    def dequeueCharacter(self):
        if len(self.queue) >= 1:
            item = self.queue[0]
            del self.queue[0]
            # Auto shift left for deletion in a python list!
            #for i in range(1,len(self.queue)):
            #    self.queue[i-1] = self.queue[i]
            #print "out",item, self.queue
            return item


# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l / 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")    
    
        
        
        
