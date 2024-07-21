class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        dirSeparator = "/"
        moveUpDir = ".."
        currentDir = "."

        pathDirs = path.split(dirSeparator)

        for i in range(len(pathDirs)):
            if pathDirs[i] == dirSeparator or pathDirs[i] == currentDir:
                pass
            elif pathDirs[i] == moveUpDir:
                if stack:
                    stack.pop()
            else:
                if pathDirs[i]:
                    stack.append(pathDirs[i])
        
        return dirSeparator + dirSeparator.join(stack)
