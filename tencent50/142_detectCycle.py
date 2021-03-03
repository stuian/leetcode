# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            a = fast.val
            b = slow.val
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
            a = fast.val
            b = slow.val
        return fast

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
    result = test.detectCycle(a)
    print(result)

if __name__ == '__main__':
    main()