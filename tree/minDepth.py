from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([])
        queue.append(root)
        count = 0
        final_count = -1
        while len(queue) != 0:
            count += 1
            nums = len(queue)
            for i in range(nums):
                node = queue.popleft()
                if not node.left and not node.right:
                    final_count = count
                    break
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if final_count > 0:
                break
        return final_count

def main():
    test = Solution()
    a = TreeNode(3)
    a.left = TreeNode(1)
    a.right = TreeNode(4)
    b = a.left
    b.right = TreeNode(2)
    print(test.minDepth(a))


if __name__ == '__main__':
    main()