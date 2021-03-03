# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        def DFS(root):
            if not root:
                return 0
            left_height = DFS(root.left)
            right_height = DFS(root.right)
            if abs(left_height - right_height) > 1:
                self.flag = False
            return max(left_height,right_height) + 1
        temp = DFS(root)
        return self.flag

def main():
    test = Solution()
    a = TreeNode(3)
    a.left = TreeNode(1)
    a.right = TreeNode(4)
    b = a.left
    b.right = TreeNode(2)
    print(test.isBalanced(a))


if __name__ == '__main__':
    main()