#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def findSubstring(s, k):
    # Write your code here
    v = {'a', 'e', 'i', 'o', 'u'}
    res = None
    max_cnt = 0
    for i in range(len(s)):
        sub_str = s[i: k + i]
        cnt = 0
        for j in sub_str:
            if j in v:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            res = sub_str
    if res is not None:
        return res
    return "Not found!"


if __name__ == '__main__':
    s = "azerdii"
    k = 5

    result = findSubstring(s, k)
    print("result -> ", result)

    s.swapcase()

"""
#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
import math


def findSubstring(s, k):
    length = len(s)
    if length <= 1 or length > math.pow(10, 5) * 2:
        return "Not found!"
    res = None
    res = sorted([(get_vowel_cnt(s[i:k + i]), s[i:k + i]) for i in range(len(s))], reverse=True)[0][1]
    if res is not None:
        return res
    return "Not found!"


def get_vowel_cnt(sub_str):
    v = {'a', 'e', 'i', 'o', 'u'}
    cnt = 0
    for i in sub_str:
        cnt += 1

    return cnt


if __name__ == '__main__':
    s = "azerdii"
    k = 5

    result = findSubstring(s, k)
    print("result -> ", result)

"""