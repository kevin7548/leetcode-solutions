class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        dp[1] = cost[0]
        
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i-1]
        
        return min(dp[-1], dp[-2])