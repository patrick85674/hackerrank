
# HackerRank challenge: alphabet-rangoli


def rangoli(size: int) -> str:
    text: str = ''
    length = 2 * size - 1
    for line in range(length):
        for c in range(length):
            if size - abs(c - size + 1) <= abs(line - size + 1):
                text += '-'
            else:
                p = abs(c - size + 1) + abs(line - size + 1)
                text += chr(ord('a') + p)
            if c + 1 < length:
                text += '-'
        if line + 1 < length:
            text += '\n'
    return text


def print_rangoli(size):
    if size <= 0:
        print("Size of rangoli has to be greater zero!")
        return
    print(rangoli(size))


print_rangoli(1)
print()
print_rangoli(2)
print()
print_rangoli(3)
print()
print_rangoli(4)
print()
print_rangoli(5)
