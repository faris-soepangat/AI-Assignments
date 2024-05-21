Assignment 1
ReadMe file
Implement a program that can find a route between any two cities using state space search
Due March 1, 2024

Student Name and Student ID: Faris Soepangat 1001374988
Programming Language Used: Python 3.12.0
This was not compiled on omega

How the code is structured: 

imported libraries:
import sys
from collections import defaultdict

1: def buildDirectedGraph(edgesList):
- This is a function that generates a directed graph from an input array

2: def deriveSuccessors(node, mapping):
- This is the function that expands the current node and return its successors

3: def traceBack(goal, pathRecord, mapping):
- This is a function that traces and prints the path from the goal to the start

4: def ucs(mapping, startPoint, endPoint):
- This is the uniform cost search algorithm

5: Main code
- Stored command line arguments into variables
- Opened/read file depending on how many arguments were typed in from the user
- Store file into 2d dictionary
- print result
- close file

How to run the code: 
1: install python3 if not already installed on your computer
2: go to the directory where the folder is located and open terminal
3: compile code by typing the following in the command line: 
   python3 find_route.py input1.txt pointA pointB or
   python3 find_route.py input1.txt pointA pointB h_kassel.txt
   (replace pointA and pointB with city names)