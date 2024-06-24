from typing import List


def sortColors(nums: List[int]) -> List:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    print(sortColors([3, 1, 5, 3, 7, 3, 5]))
