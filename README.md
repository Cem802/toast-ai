# Toast Planning Project

This project contains several Python scripts related to planning a sequence of actions to make toast. I implemented the solution in three diffuculites which are seperated in three different files.

## Files

### util.py

This file includes helper classes that are used by the toast planning scripts. These include classes that represent Nodes for search algorithms and also different kinds of Frontiers for three search algorithms, 
Breadth-first search, Depth-first search and heuristic search.

### toast_planning.py

This is the easiest version of the toast planning script. It uses breadth-first search for planning a sequence of actions to make toast. It does not take the parameter "time" into account, and just 
returns a sequence that will result in the goal state.

### toast_planning2.py

This is the second difficulty version of the toast planning script. It uses depth-first search with some conditional statements for planning a sequence of actions to make toast in the quickest "time" possible.

### toast_planning3.py

This is the hardest difficulty version of the toast planning script. It uses heuristic search with heap list for planning a sequence of actions to make toast in the quickest "time" possible and find the sequence
as fast as possible. The speed can be measured in total explored states until a solution is found. The heuristic function tries to estimate the remaining time to reach the goal if a certain path
is chosen. It also penalizes some states to avoid them as they are most likely the wrong path, like for example if the states reverses an action. The heap list ensures that when the search algorithm picks
a node from the frontier, it chooses the one with the least cost. The cost is calculated by summing the result from the heuristic function and the cost of node itself, which represents how much it costed to reach
that node. This script returns a sequence that has the lowest possible "time" parameter while exploring the least possible states.

## Run locally

Running this locally is pretty easy. First clone this repository on your machine. You might need to install heapq. There are test cases at the end of each file, so you just need to execute the files. 
Then you can see in your console what sequence it found and how much time it accumulates to. With the hardest difficulty version you will also see the amount of explored states.
