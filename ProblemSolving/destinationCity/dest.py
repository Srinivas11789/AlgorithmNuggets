class Solution(object):
    def destCity(self, pathss):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        
        # Logic 1: Built graph using dic and iterate for null dsts --> 100 pass 88% faster
        
        # Source --> Destination Map
        paths = {}
        
        # Build graph
        for (src, dst) in pathss:
            if src not in paths:
                paths[src] = []
            if dst not in paths:
                paths[dst] = []
            paths[src].append(dst)
        
        # find the src with no dsts
        for src in paths.keys():
            if paths[src] == []:
                return src
        
        return None
