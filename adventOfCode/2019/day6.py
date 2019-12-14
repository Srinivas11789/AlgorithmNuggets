"""
--- Day 6: Universal Orbit Map ---
You've landed at the Universal Orbit Map facility on Mercury. Because navigation in space often involves transferring between orbits, the orbit maps here are useful for finding efficient routes between, for example, you and Santa. You download a map of the local orbits (your puzzle input).

Except for the universal Center of Mass (COM), every object in space is in orbit around exactly one other object. An orbit looks roughly like this:

                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /
In this diagram, the object BBB is in orbit around AAA. The path that BBB takes around AAA (drawn with lines) is only partly shown. In the map data, this orbital relationship is written AAA)BBB, which means "BBB is in orbit around AAA".

Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the download. To verify maps, the Universal Orbit Map facility uses orbit count checksums - the total number of direct orbits (like the one shown above) and indirect orbits.

Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can be any number of objects long: if A orbits B, B orbits C, and C orbits D, then A indirectly orbits D.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
Visually, the above map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 7 orbits.
COM orbits nothing.
The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data?

Your puzzle answer was 358244.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a minimum of 4 orbital transfers are required:

K to J
J to E
E to D
D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)

Although it hasn't changed, you can still get your puzzle input.
"""

# Python Implmentation of day 6

def solve_problem():
    return ""

def main():
    day = "6"
    print("Day "+ day + " problem solver: ")
    
    files = [".input", ".example", ".example2"]

    for f in files:
        # Get input for problem
        content = open("day"+day+f).readlines()

        # Create a graph for the inputs
        graph = {}

        # Iterate through the inputs to create the graph with relations
        for c in content:
            core, direct_orbit = c.split(")")
            core = core.strip()
            direct_orbit = direct_orbit.strip()
            if direct_orbit not in graph:
                graph[direct_orbit] = []
            graph[direct_orbit].append(core)
        
        #print(graph)

        # Total number of edges
        edges = 0 

        for node in graph:
            stack = graph[node][:]
            curr_edge = 0
            while stack:
                current = stack.pop(0)
                curr_edge += 1
                if current in graph:
                    stack.extend(graph[current])
            edges += curr_edge
            #print(node, curr_edge)
        
        print("Day 6 Part 1 " + f + " answer is " + str(edges))

        if "YOU" in graph:

            # Logic 1: Traceback until intersection --> this assumes both the sides are of same length which is wrong
            """
            left = graph["YOU"][0]
            right = graph["SAN"][0]
            orbital_transfers = 0

            while left != right and left in graph and right in graph:
                orbital_transfers += 1
                print(left, right)
                left = graph[left][0]
                right = graph[right][0]
            """

            # Logic: Find the path of SAN and YOU until the end and find intersection --> this would be a worst case solution
            orbital_transfers = 0
            left = "YOU"
            left_path = []
            while left in graph:
                left = graph[left][0]
                left_path.append(left)
            
            right = "SAN"
            right_path = []
            while right in graph:
                right = graph[right][0]
                right_path.append(right)

            i = 0
            while i < len(left_path):
                if left_path[i] in right_path:
                    break
                else:
                    i += 1

            orbital_transfers = i + right_path.index(left_path[i])    

            print("Day 6 Part 2 " + f + " answer is " + str(orbital_transfers))
        


main()
    

        

