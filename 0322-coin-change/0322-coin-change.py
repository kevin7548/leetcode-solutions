class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):  # i: 총합
            for coin in coins:
                if coin <= i and dp[i - coin] != float('inf'):  # dp[i - coin] 조건은 보충
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1