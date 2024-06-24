import math
from collections import deque, defaultdict
from typing import List

memo = {}


class Solution:
    # BSF Solution
    def coinChange(self, coins: List[int], amount: int) -> int:
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

    # Dynamic Programming

    def coinChangeDP(self, coins: List[int], amount: int) -> int:
        INF = math.inf
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for n in range(1, amount + 1):
            for coin in coins:
                if n - coin >= 0 and dp[n - coin] < amount + 1:
                    dp[n] = min(dp[n], 1 + dp[n - coin])
        return dp[-1] if dp[-1] != amount + 1 else -1

    def min_ignore_none(self, a: int, b: int) -> int:
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    def minimum_coins(self, coins: List[int], amount: int) -> int:
        if amount in memo:
            return memo[amount]
        if amount == 0:
            answer = 0
        else:
            answer = None
            for coin in coins:
                sub_problem = amount - coin
                if sub_problem < 0:
                    continue
                answer = self.min_ignore_none(answer, self.minimum_coins(coins, sub_problem) + 1)
        memo[amount] = answer
        return answer

    def minimum_coins_v2(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                sub_problem = i - coin
                if sub_problem < 0:
                    continue
                memo[i] = self.min_ignore_none(memo.get(i), memo.get(sub_problem) + 1)

        return memo[amount]

    def how_many_ways(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(lambda _: 0)
        memo[0] = 1

        for i in range(1, amount+1):
            memo[i] = 0
            for coin in coins:
                sub_problem = i - coin
                if sub_problem < 0 :
                    continue

                memo[i] = memo[i] + memo[sub_problem]

        return memo[amount]


if __name__ == '__main__':
    obj = Solution()
    coins = [1, 4, 5]
    amount = 13
    # print(obj.coinChange(coins, amount))
    # print(obj.coinChangeDP(coins, amount))

    # print(obj.minimum_coins(coins, amount))
    # print(obj.minimum_coins_v2(coins, amount))
    print(obj.how_many_ways(coins, amount))
