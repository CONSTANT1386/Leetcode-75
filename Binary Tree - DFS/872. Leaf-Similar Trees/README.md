## [872. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75)
- ### FirstTry: DFS
  - #### Using recursion to realize, considering the leaves situation for coding. That is no `left` or `rigth` for a node, then `append(root.val)`
  - #### Nitice: when using PYTHON in leetcode, avoiding using member variable, which is `static`, and its value won't be cleared while the test sets keep changing.
- ### DFS: Why can't?
  - #### The order of leaves appending in DFS is not right
  
