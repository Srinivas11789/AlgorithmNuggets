"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


# 100 pass
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        
        # To maintain directory of all the employees - already visited nodes list
        direc = {}
        
        # Dependancy list
        sub = []
        
        # Total priority variable
        priority = 0
        
        # Iterate the employees to fill directories and sub
        
        # Having directories to store the importance and subordinates
        for employee in employees:
            if employee.id not in direc:
                direc[employee.id] = employee
                
            # To list all the dependancies
            dep = []
            
            # Employee id match
            if employee.id == id:
                sub.append(employee.id)
                dep.extend(employee.subordinates)
            # Unvisited nodes yet, nodes to be visited in the future
            elif employee.id in sub:
                dep.extend(employee.subordinates)
                
            # Nodes that have already been visited - All the dependancies circular relationship 
            while len(dep) > 0:
                current = dep.pop()
                sub.append(current)
                if current in direc:
                    dep.extend(direc[current].subordinates)
           
        # Eradicate duplicates
        sub = list(set(sub))
        
        # Total priority
        while len(sub) > 0:
                priority += direc[sub.pop()].importance
                    
        return priority
                
        """
        #brute force - with a list
        priority = []
        sub = []
        visited = {}
        for employee in employees:
            if employee.id == id:
                priority.append(employee.importance)
                sub.extend(employee.subordinates)
                for s in sub:
                    if s in visited:
                        priority.append(visited[s])
            if employee.id in sub:
                priority.append(employee.importance)
                sub.extend(employee.subordinates)
            else:
                if employee.id not in visited:
                    visited[employee.id] = 0
                visited[employee.id] = employee.importance
                    
        return sum(priority)
        """
                
            
        
