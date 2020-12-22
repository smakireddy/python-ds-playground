import math

if __name__ == '__main__':

    # take input
    n = int(input())

    binary = ""
    cnt = 0
    max_cnt = 0

    while n > 0:
        flag = 'True'
        remainder = 0 if n % 2 == 0 else 1
        n = math.floor(n / 2)
        binary = str(remainder) + binary

        if remainder == 1 and flag:
            cnt += 1
            flag = 'True'
        else:
            flag = 'False'
            cnt = 0

        if cnt > max_cnt:
            max_cnt = cnt
    print("Binary : {}".format(binary))
    print("Count of consecutive 1's : {}".format(max_cnt))