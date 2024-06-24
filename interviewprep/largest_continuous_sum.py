from typing import List


def large_count_sum(arr: List[int]) -> int:

    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num , num)
        max_sum = max(current_sum , max_sum)

    return max_sum


if __name__ == '__main__':
    arr = [1, 2, -1, 3, 4, 10, 10, -10, -1]
    r = large_count_sum(arr)
    print(r)