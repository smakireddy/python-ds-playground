def minion_game(s):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin_count = 0
    stuart_count = 0
    for i, a in enumerate(s):
        print(a)
        if a in vowels:
            kevin_count += len(s)-i
        else:
            stuart_count += len(s)-i

    print(kevin_count)
    print(stuart_count)
    if kevin_count == stuart_count:
        print("draw")
    elif kevin_count > stuart_count:
        print("Kevin {}".format(kevin_count))
    else:
        print("Stuart {}".format(stuart_count))


if __name__ == '__main__':
    minion_game("BANANANAAAS")

