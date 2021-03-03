from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def Inorder_transversal(self, root):
        if not root:
            return
        queue = deque([])
        p = root
        while len(queue) != 0 or p: # p指针遍历整棵树
            if p:
                queue.append(p)
                p = p.left
            else:
                p = queue.pop()
                print(p.val)
                p = p.right




def main():
    test = Solution()
    a = TreeNode(3)
    a.left = TreeNode(1)
    a.right = TreeNode(4)
    b = a.left
    b.right = TreeNode(2)
    test.Inorder_transversal(a)


if __name__ == '__main__':
    main()