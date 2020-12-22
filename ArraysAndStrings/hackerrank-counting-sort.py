"""
Comparison Sorting
Quicksort usually has a running time of , but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat  (worst-case) running time, since  represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

Alternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

For example, consider an array  arr= [1,1,3,2,1]. All of the values are in the range [0...3], so create an array of zeroes, result= [0,0,0,0].
The results of each iteration follow:

i	arr[i]	result
0	1	[0, 1, 0, 0]
1	1	[0, 2, 0, 0]
2	3	[0, 2, 0, 1]
3	2	[0, 2, 1, 1]
4	1	[0, 3, 1, 1]
Now we can print the list of occurrences, 0 3 1 1 or determine the sorted array: sorted [1,1,1,2,3]

"""

import math
import os


def countingSort(arr):
    n = len(arr)
    if n > 100:
        n= 100
    result = [0] * n

    for i in arr:
        cnt = 0
        if cnt <= 100:
            result[i] = result[i]+1
            cnt += 1
        else:
            return

    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    resutl = countingSort(arr)
    print(resutl)
