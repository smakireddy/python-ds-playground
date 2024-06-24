"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0,len(s),2*k):
            a[i:i+k] = reversed(a[i:i+k])

        return "".join(a)


if __name__ == "__main__":
    obj = Solution()
    s = "abcdefg"
    k = 2
    result = obj.reverseStr(s,k)
    print(result)

    s = "zyxcbakjigfe"
    k = 3
    result = obj.reverseStr(s, k)
    print(result)
