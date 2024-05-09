# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFSgetLeaves(self,root,leaves):
        if root:
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            self.DFSgetLeaves(root.left,leaves)
            self.DFSgetLeaves(root.right,leaves)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_tree1 = []
        leaves_tree2 = []
        self.DFSgetLeaves(root1,leaves_tree1)
        self.DFSgetLeaves(root2,leaves_tree2)
        return leaves_tree1 == leaves_tree2
        


