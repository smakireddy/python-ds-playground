def removeKdigits(num: str, k: int) -> str:
    for i in range(0, k):
        if not num:
            break
        biggest = num[0]
        print(f"biggest1 -> {biggest}")
        for n in num[1:]:
            print("n -> ", n )
            print("biggest -> ",biggest )

            if n < biggest:
                break
            biggest = n
            print(f"biggest2 -> {biggest}")
        num = num.replace(biggest, '', 1).lstrip('0')
        print(f"num -> {num}")
    return num or '0'


if __name__ == '__main__':
    # print(removeKdigits("5337", 2))
    print(removeKdigits("1432219", 3))
