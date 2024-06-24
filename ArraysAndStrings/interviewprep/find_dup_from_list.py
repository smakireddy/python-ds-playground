from typing import List


def find_duplicates(nums: List[int]) -> List[int]:
    seen = set()
    duplicates = set()

    for n in nums:
        if n in seen:
            duplicates.add(n)
        else:
            seen.add(n)

    return list(duplicates)


def findDuplicates(nums:List[int])->bool:
    seen = set()
    for n in nums:
        if n in seen:
            return Treu
        else:
            seen.add(n)
    return True


# # Test cases
# import unittest
#
#
# class TestFindDuplicates(unittest.TestCase):
#
#     def test_duplicates_exist(self):
#         self.assertEqual(find_duplicates([1, 2, 3, 4, 5, 2, 6, 3]), [2, 3])
#
#     def test_no_duplicates(self):
#         self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])
#
#     def test_empty_list(self):
#         self.assertEqual(find_duplicates([]), [])


if __name__ == "__main__":
    # unittest.main()
    print(findDuplicates([1, 2, 3, 4, 5,1]))
