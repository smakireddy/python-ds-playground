from typing import List

s = "string"
s.upper()


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    first = cost[0]
    second = cost[0]
    if n < 2:
        return min(first, second)
    for i in range(2, n):
        curr = cost[i] + min(first, second)
        first = second
        second = curr

    return min(first, second)


if __name__ == '__main__':
    result = minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(result)
