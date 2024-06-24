class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n).replace("0b", "")
        i = 0
        while i < len(binary) - 2:
            if binary[i] == binary[i + 1]:
                return False

        return True

    def hasAlternatingBits1(self, n: int) -> bool:
        arr = bin(n)[2:]
        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                return False
        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.hasAlternatingBits1(24))
