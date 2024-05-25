## [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/?envType=study-plan-v2&envId=leetcode-75.)
- ### Revised1: DFS--recursion
  - #### Reconstruct a graph with bi-direction, for each edge, adding an inverse direction one
  - #### The element of the matrix is a tuple (a,b), where a is which node it connect to, b is whether it is orignial one
  - #### When traverse to a node, if it is a added edge, res += 0, otherwise, += 1
- ### Revised2: DFS--realized by stack
