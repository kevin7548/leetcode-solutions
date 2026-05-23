# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        h = []
        for i, ls in enumerate(lists):
            if ls:
                heapq.heappush(h, (ls.val, i))  # 노드들은 넣지 않고 값들만 튜플에 삽입
        result = ListNode(0)    # dummy node
        curr = result   # result 대신 curr 복사본 써야. 처음과 끝 따로 추적
        while h:
            val, i = heapq.heappop(h)
            curr.next = lists[i]
            # curr, lists[i] 다음 노드로
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
        return result.next

        