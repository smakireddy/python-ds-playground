from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)+1):
            result = i
            print(nums)
            if i in nums:
                nums.pop(nums.index(i))
            else:
                return i

        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [0,1]
    print(sol.missingNumber(nums))
