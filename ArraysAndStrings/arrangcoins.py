"""
Arranging Coins
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.
Example 1:
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n in [0, 1]: return n

        count = 1
        while n > 0:
            n = n - count
            if n - count < 0:
                break
            count += 1

        return count - 1

    def arrageCoinsUsingBinarySearch(self, n: int) -> int:

        start = 1
        end = n

        while start <= end:
            mid = start + (end - start) // 2
            if (mid * (mid + 1) // 2) <= n:
                start = mid + 1
            else:
                end = mid - 1

        return end

    def arrangeCoinsSimple(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n <= 2:
            return 1

        count = 1
        while n > 0:
            n = n - count
            if n < 0:
                break
            count += 1
        return count - 1


if __name__ == '__main__':
    obj = Solution()
    # print(obj.arrangeCoins(8))
    # print(obj.arrageCoinsUsingBinarySearch(8))

    print(obj.arrangeCoinsSimple(5))
    print(obj.arrangeCoinsSimple(3))
