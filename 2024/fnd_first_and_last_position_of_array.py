from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)

        return [left, right]

    def binarySearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = l + ((r-l) // 2)
            print(f"middle num : {m}")
            if target > nums[m]:
                r = m + 1
            elif target < nums[m]:
                l = m - 1
            else:
                return m
                # if leftBias:
                #     r = m - 1
                # else:
                #     l = m + 1
        return i


if __name__ == '__main__':
    obj = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    # res = obj.searchRange(nums, target)
    res = obj.binarySearch(nums, target, False)
    print(res)
