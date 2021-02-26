from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        pass

    # def finder(self, arr1: List[int], arr2: List[int]):
    #     for i in arr1:
    #         if i not in arr2:
    #             return i

    def finder(self, arr1: List[int], arr2: List[int]):
        arr1.sort()
        arr2.sort()

        for i, j in zip(arr1, arr2):
            if i != j:
                return i

    def finder2(self, arr1: List[int], arr2: List[int]):
        d = defaultdict(int)
        for num in arr2:
            d[num] += 1

        for num in arr1:
            if d[num] == 0:
                return num
            else:
                d[num] = -1

    def finder3(self, arr1: List[int], arr2: List[int]):
        result = 0
        for num in arr1 + arr2:
            result ^= num

        return result


if __name__ == '__main__':
    obj = Solution()
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [3, 7, 2, 1, 4, 6]
    print(obj.finder3(arr1, arr2))
