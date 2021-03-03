# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        start = root
        while start:
            if start:
                m = start.val
            node = start
            start = None
            count = 0
            while node:
                if node.left and node.right:
                    node.left.next = node.right
                    count += 1
                    if count == 1:
                        start = node.left
                if node.left and not node.right:
                    count += 1
                    if count == 1:
                        start = node.left
                    temp = node.next
                    next_node = None
                    while temp:
                        if temp.left:
                            next_node = temp.left
                            break
                        elif temp.right:
                            next_node = temp.right
                            break
                        else:
                            temp = temp.next
                    node.left.next = next_node
                    print(next_node.val)
                if node.right:
                    count += 1
                    if count == 1:
                        start = node.right
                    temp = node.next
                    next_node = None
                    while temp:
                        if temp.left:
                            next_node = temp.left
                            break
                        elif temp.right:
                            next_node = temp.right
                            break
                        else:
                            temp = temp.next
                    node.right.next = next_node
                    if next_node:
                        n = next_node.val
                node = node.next
        return root

def main():
    test = Solution()
    a = Node(-9)
    a.left = Node(-3)
    a.right = Node(2)
    b = a.left
    b.right = Node(4)
    c = b.right
    c.left = Node(-6)
    d = a.right
    d.left = Node(4)
    d.right = Node(0)
    e = d.left
    e.left = Node(-5)
    print(test.connect(a))

if __name__ == '__main__':
    main()