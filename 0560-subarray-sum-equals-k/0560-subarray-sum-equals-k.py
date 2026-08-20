from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        s = defaultdict(int)    # {prefix_sum: 등장 횟수}
        s[0] = 1

        for num in nums:
            prefix_sum += num
            # 조회 먼저
            count += s[prefix_sum - k]
            # 삽입 나중
            s[prefix_sum] += 1

        return count