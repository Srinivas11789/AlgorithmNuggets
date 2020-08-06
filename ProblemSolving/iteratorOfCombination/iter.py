# Logic 1: Using itertools to get all combinations - 100 pass 86% faster
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        import itertools
        self.combinations = list(map("".join, itertools.combinations(characters, r=combinationLength)))

    def next(self) -> str:
        return self.combinations.pop(0)

    def hasNext(self) -> bool:
        if self.combinations:
            return True
        return False

# Logic 2: Without itertools with iterator?

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
