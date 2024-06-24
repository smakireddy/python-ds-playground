
# write function to see pallendrom
# s = "racecar"

# input[::-1]
#
def solution (input:str):
    result = [] # ['r','a','
    for i in reversed(range(len(input))):
        result.append(input[i])

    if input == "".join[i for i in result]:
        return True
    else:
        return False

def solution1(input:str):
    mid = len(input)//2
    first = input[:mid]
    second = input[mid+1:]
    reverse_second = reversed(second)
    if first == rever_second:
        return True
    else:
        return False

if __name__ == '__main__':
    s = "racecar"
    print(solution(s))




