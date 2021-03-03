# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.max_sum = float("-inf")
        def dfs(root):
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            max_sum = max(self.max_sum,root.val+l+r)
            return max(0,max(l,r) + root.val)
        return self.max_sum


