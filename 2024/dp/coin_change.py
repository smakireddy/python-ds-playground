"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
"""
from typing import List
from collections import deque





class Solution:

    # DP
    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for n in range(1, amount + 1):
            for coin in coins:
                if n - coin >= 0 and dp[n - coin] < amount + 1:
                    dp[n] = min(dp[n - coin] + 1, dp[n])

        return dp[-1] if dp[-1] != amount + 1 else -1

    # BSF Solution
    def coinChangeBSF(self, coins: List[int], amount: int) -> int:
        q = deque([(amount, 0)])
        seen = {amount}
        while q:
            accum_amount, num_coins = q.popleft()
            if accum_amount == 0:
                return num_coins
            for coin in coins:
                if accum_amount - coin >= 0 and accum_amount - coin not in seen:
                    q.append((accum_amount - coin, num_coins + 1))
                    seen.add(accum_amount - coin)

        return -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                sub_problem = i - coin
                if sub_problem < 0:
                    continue
                memo[i] = self.min_ignore_none(memo.get(i), memo.get(sub_problem) + 1)

        return memo[amount]

    def min_ignore_none(self,a,b):
        if a is None:
            return b
        if b is None:
            return a
        return min(a,b)


if __name__ == '__main__':
    obj = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(obj.coinChange(coins, amount))
