class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        
        
        # Logic 1: BackTrack Logic to exit when condition is not satisfied - 100 pass 5% faster
        
        # Recursive backtrack
        def backtrack(current_team, remaining):
            # Exit criteria for team of size 3
            if len(current_team) == 3:
                self.teams.append(current_team)
            else:
                # Create team
                for i in range(len(remaining)):
                    # We cant decide when team size if only 1 so just add
                    if len(current_team) == 1:
                        backtrack(current_team + [remaining[i]], remaining[i+1:])
                    else:
                        # Find if the logic is decreasing or increasing rating
                        validate = current_team[-2] > current_team[-1]
                        # Add next member to team based on increasing or decreasing criteria
                        if validate and remaining[i] < current_team[-1]:
                            backtrack(current_team + [remaining[i]], remaining[i+1:])
                        elif not validate and remaining[i] > current_team[-1]:
                            backtrack(current_team + [remaining[i]], remaining[i+1:])
            return
            
        self.teams = []
        # Usecase for every new member added to the team as the first person
        for i in range(len(rating)):
            backtrack([rating[i]], rating[i+1:])
        #print(self.teams)
        return len(self.teams)
        
