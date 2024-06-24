"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

0 1 2 3 4 5 6 7
a b c a b c b b
i

seen : { a : 0
         b : 1
         c : 1


"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = start = 0
        for ind, val in enumerate(s):
            # print(ind, val)
            if val in seen and start <= seen[val]:
                start = seen[val] + 1
            else:
                max_length = max(max_length, ind - start + 1)
            seen[val] = ind

        return max_length

    def lengthOfLongestSubstring1(self, s: str) -> int:
        seenDict = {}
        max_length = start = 0
        for i in range(len(s)):
            if s[i] in seenDict and start <= seenDict[s[i]]:  #
                start = seenDict[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)  # 0 - 0 +1

            seenDict[s[i]] = i

        return max_length


if __name__ == '__main__':
    obj = Solution()
    s = "abcabcbb"
    print(obj.lengthOfLongestSubstring(s))
