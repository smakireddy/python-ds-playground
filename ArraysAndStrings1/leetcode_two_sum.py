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

    def pair_sum(self, nums:List[int], target:int):
        if len(nums) < 2:
            return

        seen = set()
        output = set()
        for num in nums:
            k = target - num
            if k in seen:
                output.add((min(num, k), max(num,k)))
            else:
                seen.add(num)

        print ("\n".join(map(str,list(output))))


if __name__ == '__main__':
    obj = Solution()
    # arr = [2, 7, 8, 17]
    # target = 9
    arr = [1,3,2,2]
    target = 4
    # print(obj.twoSum(arr, target))
    obj.pair_sum(arr,target)

