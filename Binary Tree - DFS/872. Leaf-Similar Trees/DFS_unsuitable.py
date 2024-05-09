# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def BFSgetLeaves(self,root,leaves):
        if not root:
            return
        queue = [root]
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
                if not node.left and not node.right:
                    leaves.append(node)
            queue = tmp
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_tree1 = []
        leaves_tree2 = []
        self.BFSgetLeaves(root1,leaves_tree1)
        self.BFSgetLeaves(root2,leaves_tree2)
        return leaves_tree1 == leaves_tree2
        
# leaves_tree1:[[6],[9],[8],[7],[4]]
# leaves_tree2:[[6],[7],[4],[9],[8]]

