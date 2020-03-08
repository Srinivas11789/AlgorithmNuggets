# Logic 1: 100 pass - 81% faster - Straighforward without considering a number of complex cases makes this pass. Just take care of .. or . alone. Considering /... kind of confuses the situation
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] # Container to hold the answer, should start with /
        no_entries = set(["", "..", "."]) # No entries in result with respect to these values
        elements = path.split("/") # Split by hashes to remove single or multiple hash
        for ele in elements:
            if stack and ele == "..": # indicates we should go back on dir
                stack.pop()
            elif ele not in no_entries:
                stack.append(ele)
        stack = "/" + "/".join(stack)
        return stack
