# Logic: naive graph traversal and shortest time calc per node
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        self.graph = {}
        
        # 1. construct graph and compute times
        for time in times:
            
            src = time[0]
            dst = time[1]
            t = time[2]
            
            if src not in self.graph:
                self.graph[src] = []
            self.graph[src].append((dst, t))
            
        #print(self.graph)
            
        # 2. traverse graph
        def traverse(current, time, visited):
            
            val, t = current
            
            full_time = time + t
                                
            if self.times[val] == -1:
                self.times[val] = full_time
            elif full_time < self.times[val]:
                self.times[val] = full_time
            else:
                return
            
            if val in self.graph:
                for nxt in self.graph[val]:
                    nval, ntime = nxt
                    
                    if nval in visited:
                        continue
                    if self.times[nval] != -1 and full_time+ntime >= self.times[nval]:
                        continue
                        
                    traverse(nxt, full_time, visited.union({nval}))
            else:
                return
            
            return
        
        # 3. check all paths from k
        #if k not in self.graph:
        #    return -1
        
        """
        for i in range(1, n+1):
            if k == i:
                continue
            path_time = traverse((k,0), i, 0, set())
            #print(i, path_time)
            if path_time == 0:
                return -1
            if path_time > self.max_time:
                self.max_time = path_time
        """

        self.times = [-1]*(n+1)
        traverse((k,0), 0, set())
        
        #print(self.times)
        self.times[k] = 0
        self.times = self.times[1:]
        
        self.max = 0
        for i in self.times:
            if i == -1:
                return -1
            if i > self.max:
                self.max = i
        return self.max
