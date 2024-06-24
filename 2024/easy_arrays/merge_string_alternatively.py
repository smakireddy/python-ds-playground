"""
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1),len(word2))):
            res += word1[i]
            res += word2[i]

        if len(word1) > len(word2):
            res += word1[i+1:]
        elif len(word1) < len(word2):
            res += word2[i + 1:]

        print("current value of i =>",i)
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.mergeAlternately("abc","pqrxyz"))



