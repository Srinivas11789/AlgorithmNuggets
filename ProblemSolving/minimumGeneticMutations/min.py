class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        # ref
        bank = set(bank)
        self.mini = float('inf')
        
        def backtrack(current, visited):
            print(current, visited)

            if current == endGene:
                self.mini = min(self.mini, len(visited))
                return

            for i in range(len(current)):
                for select in ["A", "C", "G", "T"]:
                    result = current[:i] + select + current[i+1:]
                    print(current, result)
                    if result not in bank:
                        continue
                    if result in visited:
                        continue
                    backtrack(result, visited | {result})

            return


        if startGene == endGene:
            return 0

        backtrack(startGene, set())

        if self.mini == float('inf'):
            return -1
        return self.mini
