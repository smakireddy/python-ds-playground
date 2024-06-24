"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        # [1,2,3,1]
        # output : 4
        # [1,2,4,0]
        # 3 + max()
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

    def rob2(self,nums:List[int])-> int:
        rob1,rob2 = 0, 0

        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


if __name__ == '__main__':
    obj = Solution()
    print(obj.rob2([2,7,9,3,1]))