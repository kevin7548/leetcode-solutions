from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array = []
        
        counts = Counter(nums)
        frequency_list = counts.most_common(k)

        for i in range(k):
            array.append(frequency_list[i][0])
        
        return array