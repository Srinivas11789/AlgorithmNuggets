class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        
        highPopular = 0
        relation = {}
        
        for i in range(len(creators)):
            
            if creators[i] not in relation:
                relation[creators[i]] = {}
                relation[creators[i]]["totalPopular"] = 0 
                relation[creators[i]]["highPopVal"] = 0
                relation[creators[i]]["highPopIndex"] = "z"
                
            relation[creators[i]]["totalPopular"] += views[i]
            highPopular = max(relation[creators[i]]["totalPopular"], highPopular)

            #print(relation[creators[i]]["highPopIndex"], ids[i])
            if views[i] > relation[creators[i]]["highPopVal"]:
                relation[creators[i]]["highPopVal"] = views[i]
                relation[creators[i]]["highPopIndex"] = ids[i]
            elif views[i] == relation[creators[i]]["highPopVal"] and relation[creators[i]]["highPopIndex"] > ids[i]:
                relation[creators[i]]["highPopVal"] = views[i]
                relation[creators[i]]["highPopIndex"] = ids[i]    
                 
        ans = []
        visited = set()
        for i in range(len(creators)):
            if creators[i] in visited:
                continue
            if relation[creators[i]]["totalPopular"] == highPopular:
                ans.append([creators[i], relation[creators[i]]["highPopIndex"]])
                visited.add(creators[i])
                
        return ans
