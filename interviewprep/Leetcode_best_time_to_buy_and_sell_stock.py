"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit

    def maxProfit1(self, prices: List[int]) -> int:
        profits = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profits += prices[i+1] - prices[i]
        return profits

    def final_coordinates(self, moves):
        # Initialize coordinates
        x, y = 0, 0

        # Iterate through each move
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1

        return x, y


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    obj = Solution()
    print(obj.maxProfit1(prices))

    moves = 'UUUDULR'

    # Output the final coordinates
    print(obj.final_coordinates(moves))