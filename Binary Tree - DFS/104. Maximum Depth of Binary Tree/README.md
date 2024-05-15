## [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)

- ### FirstTry: DFS
  - #### The idea of recursion/ stack: we should put our emphasis on the last node(or the deepest one), that's easier to understand
  - #### For the example, for the following code, the deepest node situation is that there no more sub-nodes for the input-root, thus it will return 0, however it can't add up to the deepth. Instead it should return the max of the two sub-trees and plus 1
``` Python
def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
```

### Revised1: BFS
  - #### This idea is based on the queue
  - #### for every iteration while the queue is not empty, there are a few things as followed to be completed:
      - **Traverse the queue, add all the sub-nodes into a new queue**
      - **update the `queue` to the lastest one**
      - **add the `res` in each iteration**
  - #### Notice: the `left` or `right` of a `TreeNode` maybe `null`, thus use `if` to judge before add them to the new queue 
