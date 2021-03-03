class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merge = ListNode()
        merge.val = 0
        merge.next = None
        begin = merge
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 and l2:
            if l1.val < l2.val:
                merge.next = ListNode(l1.val)
                merge = merge.next
                l1 = l1.next
            elif l1.val > l2.val:
                merge.next = ListNode(l2.val)
                merge = merge.next
                l2 = l2.next
            else:
                merge.next = ListNode(l1.val)
                merge = merge.next
                merge.next = ListNode(l2.val)
                merge = merge.next
                l1 = l1.next
                l2 = l2.next
        if l1 is None:
            merge.next = l2
        if l2 is None:
            merge.next = l1
        merge = begin.next
        return merge

