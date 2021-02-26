from typing import List


class Solution:
    def __init__(self, arr: List[int], target: int):
        self.arr = arr
        self.target = target

    def two_sum(self) -> List[int]:
        if len(self.arr) < 2:
            return [-1, -1]

        seen = {}
        i = 0
        for n in self.arr:
            if (self.target - n) in seen.keys():
                return [seen[self.target - n], i]
            else:
                seen[n] = i
            i += 1
        return [-1, -1]


if __name__ == '__main__':
    arr = [2, 7, 8, 17]
    target = 9
    obj = Solution(arr, target)

    print(obj.two_sum())
