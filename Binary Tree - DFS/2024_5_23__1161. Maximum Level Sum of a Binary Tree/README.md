## [1161. Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)
- ### FirstTry: BFS
  - #### It is need to know, when you return the level, `level_count` increase only the next level is not null, i.e. `tmp` is not empty
- ### Revised1: DFS
  - #### The second parameter of `dfs` method, i.e. `level` is used to record the variable in recursion
  - #### `level == len(sum)` determines whether this level is firstly accessed.
