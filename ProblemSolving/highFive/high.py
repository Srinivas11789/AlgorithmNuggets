class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # Logic 1: Create a data structure Dictionary and then solve - 62% faster
        
        # Build dictionary
        students = {}
        for item in items:
            ide = item[0]
            score = item[1]
            if ide not in students:
                students[ide] = []
            students[ide].append(score)
            
        # Iterate, sort and solve
        result = []
        for k, v in students.items():
            avg = sum(sorted(v)[::-1][:5])//5
            result.append([k, avg])
        return result
        
        # Logic 2: Sort with custom logic and solve with iteration - 5% faster
        """
        def custom_cmp(x1, x2):
            # Index match first
            if x1[0] < x2[0]:
                return -1
            elif x1[0] > x2[0]:
                return 1
            else:
                # Score match next
                if x1[1] < x2[1]:
                    return 1
                else:
                    return -1
        
        # Sort with custom logic
        items = sorted(items, cmp=custom_cmp)
        
        # Iterate to compute the answer
        result = [[]]
        for i in range(len(items)):
            index = items[i][0]
            score = items[i][1]
            if len(result[-1]) == 0:
                count = 1
                result[-1] = [index, score]
            else:
                if count < 5:
                    result[-1][1] += score
                    count += 1
            if (i+1 < len(items) and items[i][0] != items[i+1][0]) or i == len(items)-1:
                result[-1][1] = result[-1][1]//5
                count = 0
                if i+1 < len(items):
                    result.append([])
        return result
        """
        
