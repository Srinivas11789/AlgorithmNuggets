# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    # Make a dictionary or hashmap of all the entries 
    # * grouping by city
    # * Sorting by time
    # * Numbering accordingly with natural numbers
    
    # Dictionary Initiate
    registry = {}
    
    # Split entries first by new line
    entries = S.split("\n")
    
    # Iterate and fill in the dictionary
    for item in entries:
        # Split by comma, 0-name, 1-city, 2-time
        #print (item.split(","))
        name, city, time = item.split(",")
        
        # Remove white spaces
        city = city.strip()
        name = name.strip()
        time = time.strip()
        
        # Insert into dict
        if city not in registry:
            registry[city] = {}
        if time not in registry[city]:
            registry[city][time] = ""
        # 2 photos at the Same time condition not mentioned in the problem, if it is also to be hanled fix by creating a list under time key
        registry[city][time] = name
    
    
    # Results dictionary
    results = {}
    
    # Sort the times and generate new name
    for city in registry:
        sortedTimes = sorted(registry[city])
        n = len(sortedTimes)
        for i in range(len(sortedTimes)):
            fullname = registry[city][sortedTimes[i]]
            name, ext = fullname.split(".")
            num = "0"*(len(str(n))-len(str(i+1)))+str(i+1)
            #registry[city][sortedTimes[i]] = city+num+"."+ext
            key = registry[city][sortedTimes[i]]+", "+city+", "+sortedTimes[i]
            results[key] = city+num+"."+ext
    
    # Reform the list of results
    #print (results)
    answer = []
    for entry in entries:
        answer.append(results[entry])
    
    return "\n".join(answer)
        
