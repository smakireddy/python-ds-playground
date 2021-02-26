# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(input())
arr = []
for i in range(n):
    number = int(input())
    arr.append(number)

# for element in arr:
#     print("processing.....", element)
#     result = "Prime"
#     if element == 1:
#         result = "Not prime"
#         print(result)
#         continue
#     sqrt = int(math.sqrt(element))
#     print("sqrt..", sqrt)
#     for i in range(2, sqrt):
#         print("element : {} , i : {}".format(element, i))
#         if element % i == 0:
#             result = "Not prime"
#             break
#
#     print(result)


for element in arr:
    for i in range(2, int(math.sqrt(element))+1):
        if element % i == 0:
            element = 1

    if element == 1:
        print("Not prime")
    else:
        print("Prime")
