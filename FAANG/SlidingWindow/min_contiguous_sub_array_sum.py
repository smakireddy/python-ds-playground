"""
Given an integer array nums and an integer k, return true if the array has a
continuous subarray of size at least two,that sums up to a multiple of k.
That is, it sums up to n * k where n is also an integer.


Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        hash_map = {0: -1}
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            rem = curr_sum % k if k != 0 else curr_sum
            if rem in hash_map and i - hash_map[rem] > 1:
                return True
            if rem not in hash_map: hash_map[rem] = i

        return False


if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6
    sol = Solution()
    print(sol.checkSubarraySum(nums, k))