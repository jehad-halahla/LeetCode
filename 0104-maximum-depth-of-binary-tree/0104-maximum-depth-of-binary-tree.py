# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    counter = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_depth(node,d):
            if node is None:
                return d
            d += 1
            return max(find_depth(node.left,d),find_depth(node.right,d))
        return find_depth(root,0)

        
        
        