from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]

    # for 루프는 list comprehension으로
    # Counter, most_common 리스트 정의 안하고 바로 사용