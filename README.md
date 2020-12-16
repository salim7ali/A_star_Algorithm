# **A star pathfinding algorithm.**
All components from the pygame grid interface to the A* pathfinding algorithm implementation were # **self implemented**.

- A Graph traversal and path search algorithm based on the Dijkstra's algorithm. Adds onto Dijkstra's algorithm by using a heuristics based approach.
- Implemented in Windows 10, py 3.6.9.
- Algorithm formula: **f(n) = g(n) + h(n)**

## **Steps to Setup:**
- Make sure to activate conda environment provided in the repo: `conda activate .\envs`
- To run application `python game.py`

## **Steps to Play:**
1.Choose Start node:
![start node](/screenshot_1.PNG?raw=true "Optional Title")

2.Choose End node:
![end node](/screenshot_2.PNG?raw=true "Optional Title")

3.Select wall nodes(currently hardcoded to 10) and path is generated using A star algorithm:
![generated path](/screenshot_3.PNG?raw=true "Optional Title")
