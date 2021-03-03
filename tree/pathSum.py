# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        queue = deque([[root]])
        res = []
        while len(queue) != 0:
            for i in range(len(queue)):
                temp = queue.popleft()
                node = temp[-1]
                if not node.left and not node.right:
                    add = 0
                    for j in temp:
                        add += j.val
                    if add == sum:
                        li = []
                        for j in temp:
                            li.append(j.val)
                        res.append(li)
                if node.left:
                    l = temp.copy()
                    l.append(node.left)
                    queue.append(l)
                if node.right:
                    l2 = temp.copy()
                    l2.append(node.right)
                    queue.append(l2)

        return res

def main():
    test = Solution()
    a = TreeNode(5)
    a.left = TreeNode(4)
    a.right = TreeNode(8)
    b = a.left
    b.left = TreeNode(11)
    c = b.left
    c.left = TreeNode(7)
    c.right = TreeNode(2)
    d = a.right
    d.left = TreeNode(13)
    d.right = TreeNode(4)
    e = d.right
    e.left = TreeNode(5)
    e.right = TreeNode(1)
    print(test.pathSum(a,22))

if __name__ == '__main__':
    main()