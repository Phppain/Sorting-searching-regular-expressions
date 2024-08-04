"""task5.py"""

def align_strings(strings):
    max_length = max(len(s) for s in strings)
    aligned_strings = [f"{'*' * (max_length - len(s))}{s}" for s in strings]
    return max_length, aligned_strings

if __name__ == "__main__":
    try:
        M = int(input("Введите количество строк: "))
    except TypeError:
        print("TypeError")
    strings = [input() for _ in range(M)]

    max_length, result_strings = align_strings(strings)

    print(max_length)
    for s in result_strings:
        print(s)
