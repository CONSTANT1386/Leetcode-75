# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum1 = []
        def dfs(node:TreeNode, level:int) -> None:      # Using level to record the current level while recursing
            if level == len(sum1):                       # Indicates it is the first time recurse to this level
                sum1.append(node.val)
            else:
                sum1[level] += node.val                  # there is the sum of the level already
            if node.left: dfs(node.left,level+1)
            if node.right: dfs(node.right,level+1)
        dfs(root, 0)                                    # the index of list is from 0
        return sum1.index(max(sum1)) + 1                # the level starts from 1
