"""
Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d


Example 1:

Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
Example 2:

Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].
Example 3:

Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5


Constraints:

4 <= nums.length <= 50
1 <= nums[i] <= 100


"""
from collections import defaultdict
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        pair_sums = defaultdict(list)
        n = len(nums)
        for i in range(1, n-2):
            for j in range(i):
                print((j,i))
                pair_sums[nums[i] + nums[j]].append((j,i))

        for k,v in pair_sums.items():
            print(f"{k}=>{v}")

        for d in range(3, n):
            for c in range(2, d):
                current_sum = nums[d] - nums[c]
                if current_sum in pair_sums:
                    print(current_sum)
                    for a, b in pair_sums[current_sum]:
                        if a < b < c:
                            count +=1

        return count


if __name__ == '__main__':
    obj = Solution()
    nums = [1,1,1,3,5]
    print(obj.countQuadruplets(nums))
