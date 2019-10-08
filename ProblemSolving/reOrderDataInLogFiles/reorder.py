class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        # Logic 1: Using dictionary datastructure to handle data and output
        l = {}
        digit = []
        
        for log in logs:
            lsplit = log.split(" ")
            # Strip identifer for key
            ident = lsplit[0]
            # Content of log
            content = " ".join(lsplit[1:])
            # Create DB entry
            if content not in l:
                l[content] = set()
            # Find out if it is digit log/ letter log
            if "".join(lsplit[1:]).isdigit():
                digit.append(log)
            else:
                l[content].add(ident)
        
        result = []
        for cont in sorted(l.keys()):
            for c in l[cont]:
                    result.append(c + " " + cont)
        result += digit
        return result
