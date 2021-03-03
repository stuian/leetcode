# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if (root) in self.memo:
            return self.memo[(root)]
        # 抢，去下下家
        do = root.val + (0 if root.left == None else self.rob(root.left.left) + self.rob(root.left.right)) + (
            0 if root.right == None else self.rob(root.right.left) + self.rob(root.right.right))
        # 不抢，去下家
        not_do = self.rob(root.left) + self.rob(root.right)
        temp = max(do, not_do)
        self.memo[(root)] = temp
        return self.memo[(root)]

