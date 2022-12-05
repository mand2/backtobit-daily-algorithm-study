# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isIdentical(root, subRoot): return True
        if not root: return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    
    def isIdentical(self, r, s) -> bool:
        if not(r and s): return r is s
        return r.val == s.val and self.isIdentical(r.left, s.left) and self.isIdentical(r.right, s.right)