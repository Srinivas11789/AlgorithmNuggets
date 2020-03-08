class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        # Logic 1: Build a graph, populate them as directed and then another loop to solve signal - Time Limit Exceeded..... but works for most of the TCs
        """
        
        # Find Path from S to E
        def signal_flow(graph, src, dst, path, time):
            path = [path] + [src]
            if src == dst:
                return path, time
            if src not in graph:
                return [], 0
            ts = []
            for node in graph[src]:
                nxt, t = node
                if nxt not in path:
                    new_path, new_time = signal_flow(graph, nxt, dst, path, time+t)
                    if new_path:
                        ts.append(new_time)
            if ts:
                return path, min(ts)
            else:
                return [],0
        
        # Graph init
        graph = {}

        # Populate the Graph
        for time in times:
            src, dst, t = time
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append([dst, t])

        # Track Signal
        if (K not in graph) or (K in graph and graph[K] == []):
            return -1
        
        if len(graph.keys()) < N:
            return -1
        
        signal = [None]*N
        signal[K-1] = 0
        all_time = 0
        
        for dest in graph.keys():
            if dest != K:
                p, signal[dest-1] = signal_flow(graph, K, dest, [], 0)
                #print(p, signal)
                if signal[dest-1] == 0:
                    return -1
                all_time = max(all_time, signal[dest-1])
            if signal[dest-1] is None:
                return -1

        return all_time
        """
        
        # Logic 2: Same gist as above with set(), dijikstra algo - 99%

        # Graph Init
        graph = {}
        
        # Graph Build
        # Populate the Graph
        for time in times:
            src, dst, t = time
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append([t, dst])
            
        visited = set()
        stack = [(0, K)]
        signal_flow = {i:float('inf') for i in range(1, N+1)}
        signal_flow[K] = 0
        
        while stack:
            c_wgt, c_node = heapq.heappop(stack)
            if c_node in visited:
                continue
            visited.add(c_node)
            if len(visited) == N:
                return c_wgt
            for n_wgt, n_node in graph[c_node]:
                new_cost = c_wgt + n_wgt
                if new_cost < signal_flow[n_node] and n_node not in visited:
                    signal_flow[n_node] = new_cost
                    heapq.heappush(stack, (new_cost, n_node))
        return -1


        
        
        
