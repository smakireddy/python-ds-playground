"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        n = len(chars)
        i = 0
        while n > 0:
            value = chars.pop(0)
            n -= 1
            chars.append(value)

            count = 1
            while n > 0:
                next_val = chars[0]
                if next_val != value:
                    break

                next_val = chars.pop(0)
                n -= 1
                count += 1

            if count != 1:
                print(f"count=>{count}")
                count = str(count)
                for i in count:
                    chars.append(i)

        return len(chars)


if __name__ == '__main__':
    obj = Solution()
    print(obj.compress(list("aabbccc")))
