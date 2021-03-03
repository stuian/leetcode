# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1_Node, l2_Node):
        if l1_Node is None:
            return l2_Node
        if l2_Node is None:
            return l1_Node

        l1 = []
        l2 = []

        while l1_Node:
            l1.append(l1_Node.val)
            l1_Node = l1_Node.next

        while l2_Node:
            l2.append(l2_Node.val)
            l2_Node = l2_Node.next

        num1 = 0
        len1 = len(l1)
        for i in range(len1):
            num1 += l1[i] * (10 ** i)

        num2 = 0
        len2 = len(l2)
        for i in range(len2):
            num2 += l2[i] * (10 ** i)

        sum = num1 + num2

        # 求位数
        count = 1
        while sum // (10 ** count) != 0:
            count += 1

        temp = []
        for i in range(count):
            if i != count - 1:
                temp.append(sum % 10)
                sum = sum // 10
            else:
                temp.append(sum)

        temp_Node = ListNode(0)
        sum_Node = temp_Node
        for i in temp:
            sum_Node.next = ListNode(i)
            sum_Node = sum_Node.next
        sum_Node = temp_Node.next
        del temp_Node
        return sum_Node