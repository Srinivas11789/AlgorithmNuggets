class Solution:
    # Logic 1: maintain rod as dicts and update counts - 85% faster
     
    def countPoints(self, rings: str) -> int:
        
        rods = [{} for i in range(11)] # maintain rods as list of dicts for easier lookup
        rod_with_all_colors = 0
        
        for r in range(0, len(rings), 2):
            
            color = rings[r]
            rod = int(rings[r+1])
            
            if color not in rods[rod]:
                rods[rod][color] = 0
                
                # check for all colors presence in a row
                if len(rods[rod]) == 3:
                    rod_with_all_colors += 1

            # this is not asked, but good to track how many color rings are there per row
            rods[rod][color] += 1
            
        return rod_with_all_colors

