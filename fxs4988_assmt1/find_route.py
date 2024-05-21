# Faris Soepangat 1001374988

import sys
from collections import defaultdict

# This is a function that generates a directed graph from an input array
def buildDirectedGraph(edgesList):

    networkMap = defaultdict(dict)
    for pointA, pointB, distance in edgesList:
        networkMap[pointA][pointB] = distance
        networkMap[pointB][pointA] = distance
    return networkMap

# This is the function that expands the current node and return its successors
def deriveSuccessors(node, mapping):

    successors = [] # the empty set to store successors

    # This finds all cities the current node is connected to
    for connection in mapping[node[0]]:
        # g(n): The distance from the start node = cost of the current node(from start) + cost of current node to child
        pathCost = node[1] + int(mapping[node[0]][connection])
        originPoint = node[0] # Stores the parent of the child (current_node) in a variable
        
        if cmdArgLength == 4:
            nextNode = [connection, pathCost, originPoint, 0, pathCost]
        elif cmdArgLength == 5:
            # Create a new node with the child and direct distance from the start
            heuristicCost = int(heuristicData[connection]) # heuristicCost is the heuristic value
            totalCost = pathCost + heuristicCost # totalCost is A* search algorithm
            nextNode = [connection, pathCost, originPoint, heuristicCost, totalCost]
        successors.append(nextNode) # Add s to successors

    return successors # returns array of successors

# This is a function that traces and prints the path from the goal to the start
def traceBack(goal, pathRecord, mapping):
    pathTaken = [] # List to store the path
    target = goal
     # This finds the index of the destination city in the pathRecord
    for step in reversed(pathRecord):
        # Traverse the pathRecord in reverse order from the destination to the origin
        if(step[0] == target and step[2] != 'start'):
            # step[2] is location1 and step[0] is location2
            pathTaken.insert(0, f"{step[2]} to {step[0]}, {float(mapping[step[2]][target]):.1f} km")
            target = step[2]

    # This prints the route in the correct order
    for segment in pathTaken:
        print(segment) 
    return " "

# This is the uniform cost search algorithm
def ucs(mapping, startPoint, endPoint):

    explored = []
    fringe = []
    pathList = []

    nodesPopped = 0 # nodes popped is initialized to 0
    nodesExpanded = 0 # nodes expanded is initialized to 0
    nodesGenerated = 0 # nodes generated is initialized to 0
    fringe.append([startPoint, 0, "start", 0, 0])
    nodesGenerated += 1

    # pops node from the fringe
    while fringe:
        currentNode = fringe.pop(0)
        nodesPopped += 1

        # Adds goal node to pathRecord 
        if currentNode[0] == endPoint:
            pathList.append(currentNode)
            print("\nNodes Popped: " + str(nodesPopped)) # prints the nodes popped
            print("Nodes Expanded: " + str(nodesExpanded)) # prints the nodes expanded
            print("Nodes Generated: " + str(nodesGenerated)) # prints the nodes generated
            print("Distance: {:.1f} km".format(float(currentNode[1]))) # prints the distance between routes
            print("Route:")
            traceBack(endPoint, pathList, mapping)
            return "\n"
        
        # Checks if current node is in the closed set
        if currentNode[0] not in explored:
            # Add current node to closed set
            explored.append(currentNode[0])
             # Expands the node
            pathList.append(currentNode)
            successors = deriveSuccessors(currentNode, mapping)
            nodesGenerated += len(successors)
            nodesExpanded += 1 
            fringe += successors

            # Uninformed (sorts by gn)
            # Informed (sorts by fn)
            fringe.sort(key=lambda x: x[1] if cmdArgLength == 4 else x[4])
    
    print("\nNodes Popped:", nodesPopped) # Prints the nodes popped
    print("Nodes Expanded:", nodesExpanded) # Prints the nodes expanded
    print("Nodes Generated:", nodesGenerated) # Prints the nodes generated
    print("Distance: infinity") # Prints that the distance is infinity
    print("Route:\nNone") # Prints that there is no route
    return " "

# Main Code starts here

# Store the command line arguments into variables
cmdArgLength = len(sys.argv)
dataFile = sys.argv[1] # data file = second command line argument
startCity = sys.argv[2] # start city = third command line argument
goalCity = sys.argv[3] # goal city = fourth command line argument

if cmdArgLength == 5:
    heuristicFile = sys.argv[4] # fifth command line argument
    # opens and reads the heuristic text file
    with open(heuristicFile, 'r') as file:
        heuristicLines = file.readlines() # stores heuristice file contents
    # removes last line of file
    heuristicData = {line.split()[0]: line.split()[1] for line in heuristicLines if line.strip() != 'END OF INPUT'}

# opens and reads the text file
with open(dataFile, 'r') as file:
    # removes last line
    edgeLines = [line.strip().split() for line in file if line.strip() != 'END OF INPUT']

# Stores the input file as a 2D dictionary
graphMap = buildDirectedGraph(edgeLines)

# Uninformed search if n = 4 or Informed search if n = 5
if cmdArgLength in [4, 5]:
    print(ucs(graphMap, startCity, goalCity))