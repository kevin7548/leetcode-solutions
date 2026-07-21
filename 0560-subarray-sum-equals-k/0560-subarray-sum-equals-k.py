class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        sum_set = {0: 1}    # {합: 개수}. 핵심은 누적합이 여러 번 나올 수 있다는 것!
        for n in nums:
            running_sum += n
            count += sum_set.get(running_sum - k, 0)
            sum_set[running_sum] = sum_set.get(running_sum, 0) + 1
        return count
        
        # 1:1, 2:1, 3:1  => k=2