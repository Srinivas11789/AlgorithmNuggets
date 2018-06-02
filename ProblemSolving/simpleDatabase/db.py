# Mistook the db transaction part of begin, rollback where I assumed that, commit applies all the group of commands entered as a list until which you never see any change in a db, similarly for rollback. Took path of logic where i could apply changes and revert them handling as a list of commands
# The real logic was to have copies of the db where you operate on, when commit is issued the changes migrate to the origin or previous version. Rollback throws away the changes

# Lesson:
# * donot assume functionality
# * look at the example test case to understand whether what you presume as the goal or objective is right and then proceed
# * Dict are mutable, use .copy() function to take a copy else the reference moves everywhere you create a copy 

class Solution(object):
    def __init__(self):
        
        # Create a dictionary or map database
        self.data = {}
        
        # Transaction nest tracking
        self.num = []

    def set(self, name, value):
        
        if self.num:
            self.num[-1]["commands"].append(("set",name,value))
            if name not in self.num[-1]["copy"]:
                self.num[-1]["copy"][name] = 0
            self.num[-1]["copy"][name] = value
        else:
            # Create a key if not present
            if name not in self.data:
                self.data[name] = 0
        
            # Assign value
            self.data[name] = value

    def get(self, name):
        
        # Get doesnt alter any data so, it can work under any transaction - no change
        #print (self.num, name, self.data)
        
        if self.num:
            if name in self.num[-1]["copy"]:
                return self.num[-1]["copy"][name]
            else:
                return 0           
        else:
            # Return the value else 0
            if name in self.data:
                return self.data[name]
            else:
                return 0


    def unset(self, name):
        
        if self.num:
            self.num[-1]["commands"].append(("unset",name))
            if name in self.num[-1]["copy"]:
                del self.num[-1]["copy"][name]
            else:
                pass
        else:
            # Delete or return nothing
            if name in self.data:
                del self.data[name]
            else:
                pass

    def count(self, value):
        
        if self.num:
            db = self.num[-1]["copy"]
        else:
            db = self.data

        # Exact count or zero
        counter = 0
        for key, val in db.items():
            if val == value:
                counter += 1
        return counter
                

    def begin(self):
        
        self.trans = {}
        if "commands" not in self.trans:
                self.trans["commands"] = []
        if "commit" not in self.trans:
                self.trans["commit"] = False
        
        if not self.num:
            if "copy" not in self.trans:
                self.trans["copy"] = self.data.copy()
            self.num.append(self.trans)        
        else:
            if "copy" not in self.trans:
                # Lesson learn - a mutable object copied alters all the nested dictionary - only the copy should be edited at every level unless commit
                self.trans["copy"] = self.num[-1]["copy"].copy()
            self.num.append(self.trans)
            
    def rollback(self):
        if self.num:
            commands = self.num[-1]["commands"]
        else:
            commands = []
        
        if not commands:
            return False
            
        # CleanUp
        self.num.pop()
        
        return True

    def commit(self):
        if self.num:
            commands = self.num[-1]["commands"]
        else:
            commands = []
        if not commands:
            return False

        if len(self.num) > 1:
            self.num[-2]["copy"] = self.num[-1]["copy"].copy()
        else:
            self.data = self.num[-1]["copy"].copy()

        # CleanUp
        self.num.pop()
            
        return True
    
def test():
        sol = Solution()
        sol.set('a', 10)
        sol.begin()
        sol.set('a', 20)
        sol.begin()
        sol.set('a', 30)
        print ("ok")
        assert sol.rollback() == True
        assert sol.get('a') == 20
        sol.begin()
        sol.set('a', 30)
        assert sol.commit() == True
        assert sol.get('a') == 30
        assert sol.rollback() == True
        assert sol.get('a') == 10
        assert sol.commit() == False

test()

