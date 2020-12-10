if __name__ == '__main__':
    s = input()
    print(s.isalnum())
    length = len(s)
    for i in range(length):
        if not s[i].isalpha():
            if i + 1 == length:
                print(False)
            continue
        if s[i].isalpha():
            print(True)
            break

    for i in range(length):
        if not s[i].isdigit():
            if i + 1 == length:
                print(False)
            continue
        if s[i].isdigit():
            print(True)
            break

    for i in range(length):
        if not s[i].islower():
            if i + 1 == length:
                print(False)
            continue
        if s[i].islower():
            print(True)
            break

    for i in range(length):
        if not s[i].isupper():
            if i + 1 == length:
                print(False)
            continue
        if s[i].isupper():
            print(True)
            break
