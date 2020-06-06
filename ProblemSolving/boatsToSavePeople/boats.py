ss Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # Greedy Approach to fill the boat to capacity as they come in
        
        # Logic 2 - Using Dictionary - 100 pass - only 5 % faster - optimize?
        import collections
        boats = 0
        p = collections.Counter(people)
        for i in range(len(people)):
            if p[people[i]] == 0:
                continue
            current = people[i]
            # IF CURRENT PERSON SATISFIES FULL WEIGHT
            if current == limit:
                p[current] -= 1
                boats += 1
            else:
                # IF WEIGHT IS LESSER SELECT BEST OPTIMAL CHOICE FOR THE CURRENT 
                next_person = limit - current
                p[current] -= 1
                while next_person and (next_person not in p or p[next_person] <=0):
                    next_person -= 1
                if next_person > 0:
                    p[next_person] -= 1
                #print(next_person, current)
                boats += 1
            #print(p, boats)
        return boats
                
        
        
        # Logic 1: Iteration with some sort - This would not work as we need to find out the exact weight matches to make current optimal choice
        """
        boats = 0
        people.sort()
        while people:
            total_weight = 0
            while total_weight < limit and people and (total_weight + people[0]) <= limit :
                total_weight += people.pop(0)
            boats += 1
            print(boats, total_weight, people)
        return boats
        """
                
                
            
        
