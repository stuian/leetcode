# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 找到链表第N个结点的前驱结点；头结点加前再加一个结点
        temp = ListNode(0)
        temp.next = head
        fast = slow = temp
        while fast and n > 0:
            n = n - 1
            fast = fast.next
        if n > 0:
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return temp.next
        
