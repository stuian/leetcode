# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swap(self, a, b):
        temp = a.val
        a.val = b.val
        b.val = temp

    def sortList(self, head):
        tail = None

        def sortList2(prev, end):
            if prev != end:
                p = prev
                q = prev.next
                key = prev.val
                while q != end:
                    b = q.val
                    if q.val < key:
                        p = p.next
                        self.swap(p, q)
                    q = q.next
                self.swap(prev, p)
                sortList2(prev, p)
                sortList2(p.next, end)

        sortList2(head, tail)

def main():
    test = Solution()
    a = ListNode(3)
    a.next = ListNode(2)
    b = a.next
    b.next = ListNode(0)
    c = b.next
    c.next = ListNode(4)
    c = c.next
    c.next = None
    test.sortList(a)

if __name__ == '__main__':
    main()
