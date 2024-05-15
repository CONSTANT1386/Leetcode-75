# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            tmp = []
            level_nodes = []
            for node in queue:
                if node:
                    if node.left: 
                        tmp.append(node.left)
                        level_nodes.append(node.left.val)
                    else: level_nodes.append(None)
                    if node.right:
                        tmp.append(node.right)
                        level_nodes.append(node.right.val)
                    else: level_nodes.append(None)

            if not level_nodes == level_nodes[::-1]:
                return False
            queue = tmp
        return True
                
            
