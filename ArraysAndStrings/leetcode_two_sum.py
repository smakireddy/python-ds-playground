"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in mydict.keys():
                return [mydict[compliment], i]
            else:
                mydict[nums[i]] = i
        return [-1, -1]


if __name__ == '__main__':
    obj = Solution()
    arr = [2, 7, 8, 17]
    target = 9
    print(obj.twoSum(arr, target))