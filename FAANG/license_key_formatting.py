class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if S is None or len(S) == 0:
            return S
        result = ""

        for s in S[::-1]:
            if s != '-':
                print(len(result) % (K + 1))
                if len(result) % (K+1) == K:
                    result += '-'
                result += s.upper()

        return result[::-1]


if __name__ == '__main__':
    obj = Solution()
    # S = "5F3Z-2e-9-w"
    S = "2-5g-3-J"
    k = 2
    print(obj.licenseKeyFormatting(S, k))
