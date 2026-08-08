# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        prev = dummy    # 현재까지 확정
        curr = head    # 검사하는 노드

        while curr:
            if curr.next and curr.val == curr.next.val:
                val = curr.val 
                while curr and val == curr.val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next