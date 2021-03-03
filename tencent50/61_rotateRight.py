class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k: return head
        temp,count = head,0
        while temp:
            count += 1
            temp = temp.next
        k = k % count
        if k == 0:
            return head
        fast = slow = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead

def main():
    test = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    result = test.rotateRight(a,2)
    print(result)

if __name__ == '__main__':
    main()