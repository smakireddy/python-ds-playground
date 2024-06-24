from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen.keys():
                return [seen[target - n], i]
            else:
                seen[n] = i
        return []


if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum([2, 7, 11, 15], 9))
