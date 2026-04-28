# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        
        def dfs(node):
            if not node:
                return True, 0, float('inf'), float('-inf')
            
            l_bst, l_sum, l_min, l_max = dfs(node.left)
            r_bst, r_sum, r_min, r_max = dfs(node.right)
            
            if l_bst and r_bst and l_max < node.val < r_min:
                total = l_sum + r_sum + node.val
                self.max_sum = max(self.max_sum, total)
                return True, total, min(node.val, l_min), max(node.val, r_max)
            else:
                return False, 0, 0, 0
        
        dfs(root)
        return self.max_sum