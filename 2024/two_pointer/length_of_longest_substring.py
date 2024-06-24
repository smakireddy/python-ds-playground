"""

Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        ans = 0
        # map store the current index of a charector
        mp = {}

        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

    def lengthOfLongestSubstring_window(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

    def lengthOfLongestSubstring_mp(self, s: str) -> int:
        mp = {}
        start = 0
        res = 0

        for end, c in enumerate(s):
            if c in mp:
                start = mp[c] + 1
                mp[c] = end
            else:
                mp[c] = end
            res = max(res, end - start + 1)
        return res


if __name__ == '__main__':
    obj = Solution()
    s = "abcabcbb"
    # print(obj.lengthOfLongestSubstring(s))
    print(obj.lengthOfLongestSubstring_window(s))
    print(obj.lengthOfLongestSubstring_mp(s))
