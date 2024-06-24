if name == 'main':
    n = int(input())
    arr = list(map(int, input().split()))
    largest = max(arr)
    i = 0
    sec_largest = arr[1]
    while i < len(arr):
        if arr[i] > sec_largest and arr[i] < largest:
         sec_largest = arr[i]
        i = i + 1
    print(sec_largest)