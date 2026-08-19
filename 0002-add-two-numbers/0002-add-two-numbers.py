# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        num1, num2 = l1, l2
        curr = dummy
        roundup = 0

        while num1 or num2 or roundup:
            v1 = num1.val if num1 else 0
            v2 = num2.val if num2 else 0
            total = v1 + v2 + roundup
            roundup = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            num1 = num1.next if num1 else None
            num2 = num2.next if num2 else None

        return dummy.next