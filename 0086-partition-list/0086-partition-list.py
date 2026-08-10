# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(0, head), ListNode(0, head)
        less, great = dummy1, dummy2

        while less.next:
            if less.next.val < x:
                less = less.next
                great.next = great.next.next
            else:
                great = great.next
                less.next = less.next.next
        
        less.next = dummy2.next

        return dummy1.next