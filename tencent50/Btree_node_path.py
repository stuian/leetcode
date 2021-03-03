# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.path = []

    def nodePath(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root or root == p:
            return root
        left = self.nodePath(root.left,p)
        right = self.nodePath(root.right,p)
        if left or right:
            self.path.append(root.val)
            return root

def main():
    test = Solution()
    a = TreeNode(3)
    a.left = TreeNode(1)
    a.right = TreeNode(4)
    b = a.left
    b.right = TreeNode(2)
    temp = test.nodePath(a,b.right)
    print(test.path) # 父节点及所有祖父节点，不包括本身节点

if __name__ == '__main__':
    main()