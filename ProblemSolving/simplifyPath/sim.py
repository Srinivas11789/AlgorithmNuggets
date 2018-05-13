class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        # 1. Dirs list separated by "/" as the slashes need to be separated
        # 2. "." have no meaning for path summarization hence we could remove them
        dirs = [d for d in path.split("/") if d and d != "."]
        
        # Iterate through the possible directories
        i = 0
        while i < len(dirs):
            
            # If ".." exist then remove entry before the directory as it goes back and delete ".." as well
            # Else iterate further
            if dirs[i] == "..":
                if i > 0:
                    del dirs[i]
                    del dirs[i-1]
                    i = i-1
                else:
                    del dirs[i]
            else:
                i += 1
        
        # return answer by joining with "/" and add a "/" in front 
        return "/"+"/".join(dirs)
        
        # Eliminating components without knowing the rules wont work, unix path rules should apply        
        """
        if ".." in dirs:
            if dirs[len(dirs)-1] == "..":
                return "/"
            else:
                return "/"+dirs[len(dirs)-1]
        else:
            if len(dirs) == 0:
                return "/"
            if len(dirs) == 1:
                    if dirs[0] == ".":
                        return "/"
                    else:
                        return "/"+dirs[0]
            else:
                return "/".join(dirs)
        """
