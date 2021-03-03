# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        # 4. 列表倒置
        if not head or not head.next:
            return False
        p, q = None, head
        while q:
            u, p, q = p, q, q.next
            p.next = u
            b = p.val
            c = q.val
        return head == p

def main():
    test = Solution()
    a = ListNode(3)
    a.next = ListNode(2)
    b = a.next
    b.next = ListNode(0)
    c = b.next
    c.next = ListNode(4)
    c = c.next
    c.next = b
    result = test.hasCycle(a)
    print(result)

if __name__ == '__main__':
    main()