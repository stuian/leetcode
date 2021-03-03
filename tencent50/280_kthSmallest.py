# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k) :
        self.k = k
        self.temp = []
        def search(tnode):
            if not tnode:
                return
            search(tnode.left)
            self.temp.append(tnode.val)
            search(tnode.right)
        search(root)
        print(self.temp)

def main():
    test = Solution()
    a = TreeNode(3)
    a.left = TreeNode(1)
    a.right = TreeNode(4)
    b = a.left
    b.right = TreeNode(2)
    test.kthSmallest(a,1)

if __name__ == '__main__':
    main()