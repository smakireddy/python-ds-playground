def sentence_reversal(s):
    words = []
    spaces = [' ']
    i = 0
    while i < len(s):
        if s[i] not in spaces:
            start_length = i
            while i < len(s) and s[i] not in spaces:
                i += 1

            words.append(s[start_length:i])
        i += 1
    return " ".join(map(str, reversed(words)))


if __name__ == '__main__':
    print(sentence_reversal("   you are good    "))