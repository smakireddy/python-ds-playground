"""
3Sum

Solution
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            if (i == 0) or (nums[i] != nums[i - 1]):
                self.twoSumII(nums, i, result)

        return result

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                res.append([nums[i], nums[l], nums[r]])
                while (l < r) and nums[l] == nums[l + 1]:
                    l += 1
                while (l < r) and nums[r] == nums[r - 1]:
                    r -= 1
            elif total > 0:
                r -= 1
            elif total < 0:
                l += 1

            l += 1
            r -= 1

    def threeSum2(self, nums:List[int]) -> List[List[int]]:
            res = []
            found = set()
            for i, val1 in enumerate(nums):
                seen = set()
                for j, val2 in enumerate(nums[i + 1:]):
                    complement = -val1 - val2
                    if complement in seen:
                        min_val = min((val1, val2, complement))
                        max_val = max((val1, val2, complement))
                        if (min_val, max_val) not in found:
                            found.add((min_val, max_val))
                            res.append([val1, val2, complement])
                    seen.add(val2)
            return res




if __name__ == '__main__':
    obj = Solution()
    # result = obj.threeSum([-8,-7,5,2,2])
    result = obj.threeSum2([-1, 0, 1, 2, -1, -4])
    print(result)
