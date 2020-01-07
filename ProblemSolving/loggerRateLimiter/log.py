# Logic 1: Using dictionary to store message and timestamp - 100 pass - 92% faster
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # Track message with the second it was first displayed
        # "message": "seconds of first display"
        self.messages = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        
        if message in self.messages and timestamp-self.messages[message] < 10:
            return False
        else:
            self.messages[message] = timestamp
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
