# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        prev, curr = dummy, head

        while curr:
            if curr.next and curr.val == curr.next.val:
                value = curr.val
                while curr and curr.val == value:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next    # curr가 마지막 노드면 none으로 이동
        
        return dummy.next
