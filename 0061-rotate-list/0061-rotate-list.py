# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        tail.next = head    # tail 끝 연결하기

        k %= length
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None    # new tail 끝 삭제
        return new_head