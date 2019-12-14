# Logic 1: with hashmap and binary search --> still time limit exceeded, fix it...
"""
class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        # Create key if it does not exist
        if key not in self.dict:
            self.dict[key] = {}
        
        # Else add the timestamp to the key dictionary
        if timestamp in self.dict[key]:
            return "Error"
        
        self.dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        
        def binary_search(timestamps, timestamp):
            left = 0
            right = len(timestamps)-1
            if right == left:
                if timestamp >= timestamps[left]:
                    return left
            while left < right:
                mid = (right + left)//2
                #print(left, mid, right, timestamps, timestamp)
                if timestamps[mid] == timestamp:
                    return mid
                elif timestamps[left] == timestamp:
                    return left
                elif timestamps[right] == timestamp: 
                    return right
                elif timestamps[mid] < timestamp:
                    left = mid
                else:
                    right = mid
                
                if right-left == 1:
                    if timestamp > timestamps[right]:
                        return right
                    elif timestamp > timestamps[left]:
                        return left
                    else:
                        return None
                    
        # Error if key does not exist
        if key not in self.dict:
            return ""
        
        timestamps = list(self.dict[key].keys())
        
        # Logic 1: to search through the timestamp: causes time limit exceeded on last tc but passes others
        
        #while len(timestamps) > 0 and timestamps[-1] > timestamp:
        #    timestamps.pop()
        
        #if not timestamps:
        #    return ""
        
        
        # Logic 2: Use Binary Search
        last_time = binary_search(timestamps, timestamp)
        
        #if last_time:
        #    print(timestamps, timestamp, last_time, self.dict[key][timestamps[last_time]])
        #else:
        #    print(timestamps, timestamp, last_time)
        
        if last_time == None:
            return ""
        
        return self.dict[key][timestamps[last_time]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
"""

# Logic 2: Change the data structure arragements to make it faster... --> 100 pass

class TimeMap:

    def __init__(self):
        self.dict = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.dict:
            self.dict[key] = [[],[]]
        
        self.dict[key][0].append(timestamp)
        self.dict[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        
        def binary_search(timestamps, timestamp):
            left = 0
            right = len(timestamps)-1
            if right == left:
                if timestamp >= timestamps[left]:
                    return left
            while left < right:
                mid = (right + left)//2
                #print(left, mid, right, timestamps, timestamp)
                if timestamps[mid] == timestamp:
                    return mid
                elif timestamps[left] == timestamp:
                    return left
                elif timestamps[right] == timestamp: 
                    return right
                elif timestamps[mid] < timestamp:
                    left = mid
                else:
                    right = mid
                
                if right-left == 1:
                    if timestamp > timestamps[right]:
                        return right
                    elif timestamp > timestamps[left]:
                        return left
                    else:
                        return None
                    
        # Error if key does not exist
        if key not in self.dict:
            return ""
        
        # Logic 2: Use Binary Search
        last_time = binary_search(self.dict[key][0], timestamp)
        
        if last_time == None:
            return ""
        
        return self.dict[key][1][last_time]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
