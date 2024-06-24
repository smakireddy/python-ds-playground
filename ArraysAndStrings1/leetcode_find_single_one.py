from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashtable = {}

        for i in nums:
            if i in hashtable.keys():
                hashtable[i] += 1
            else:
                hashtable[i] = 1

        # result = [key for key, val in hashtable.items() if val == 1][0]
        return [key for key, val in hashtable.items() if val == 1][0]

    # def singleNumberWithXOR(self, nums: List[int]) -> int:
    #     r = 0
    #     for i in nums:
    #         r ^= i
    #
    #     return r
    #
    # def singleNumberWithMath(self,nums: List[int])->int:
    #     print(set(nums))
    #     print(sum(list(nums)))
    #     print(sum(nums))
    #     result = (2 * (sum(set(nums)))) - (sum(nums))
    #
    #     return result//2


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 3, 2, 2, 3, 3, 3, 4, 2, 2, 2]))
    # print(s.singleNumber([2,2,3,2]))
    # print(s.singleNumberWithXOR([2, 2, 3, 2]))
    # print(s.singleNumberWithMath([2,2,3,2]))
    # print(s.singleNumberWithMath([2, 2, 3, 2, 2, 3, 3, 3, 4, 2, 2, 2]))