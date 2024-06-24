def solution(N):
    for i in range(N-1):
        print('L')
    arr = ['L' for _ in range(N)]
    print(''.join(arr))
if __name__ == '__main__':
    solution(10)