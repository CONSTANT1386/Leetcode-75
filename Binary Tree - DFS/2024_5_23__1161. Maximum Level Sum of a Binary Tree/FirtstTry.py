# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        queue = [root]
        max_level, level_count = 1, 1
        while queue:
            tmp = []
            level_sum = 0
            for node in queue:
                if node.left: 
                    tmp.append(node.left)
                    level_sum += node.left.val
                if node.right:
                    tmp.append(node.right)
                    level_sum += node.right.val
            queue = tmp
            if queue:
                level_count += 1
                if level_sum > maxSum:
                    max_level = level_count
                    maxSum = level_sum
        return max_level
