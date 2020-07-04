class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # Logic 1: Naive Iterate N times for N days - All pass except scale case - TIME LIMIT EXCEEDED
        """
        n = len(cells)
        while N:
            #print(cells)
            nxt_day = cells[:]
            for i in range(1, n-1):
                left = cells[i+1]
                right = cells[i-1]
                if left == right:
                    nxt_day[i] = 1
                else:
                    nxt_day[i] = 0
                nxt_day[0] = 0
                nxt_day[n-1] = 0
            cells = nxt_day
            N -= 1
        return cells
        """
        
        # Logic 2: 
        # * There are only a finite number of combinations or arrangement possible, after that it would rotate to follow the same pattern. We just find out how much combination is possible and divide that by N to just return what would be after the N days. 
        # * we iterate until we find the loop and with math we can return the expected
        n = len(cells)
        visited = []
        nxt_day = None
        while not visited or visited[0] != nxt_day:
            if nxt_day:
                visited.append(nxt_day)
            nxt_day = cells[:]
            for i in range(1, n-1):
                left = cells[i+1]
                right = cells[i-1]
                if left == right:
                    nxt_day[i] = 1
                else:
                    nxt_day[i] = 0
                nxt_day[0] = 0
                nxt_day[n-1] = 0
            print(visited, nxt_day)
            if visited and nxt_day == visited[0]:
                break
            cells = nxt_day
            N -= 1
        print(len(visited))
        N = N%len(visited)
        print(N, visited[N-1])
        return visited[N-1]
        
