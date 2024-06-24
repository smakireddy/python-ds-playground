"""
 Minimum Size Subarray Sum

 Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105

"""

import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = sys.maxsize
        sums = 0
        for right in range(len(nums)):
            sums += nums[right]

            while sums >= target:
                ans = min(ans, right + 1 - left)
                sums -= nums[left]
                left = left + 1

        return ans if ans != sys.maxsize else 0


if __name__ == '__main__':
    sol = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(sol.minSubArrayLen(target, nums))
