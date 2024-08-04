"""task4.py"""

def find_closest_pair(numbers):
    numbers.sort()
    min_diff = float('inf')
    pair = (None, None)
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            pair = (numbers[i], numbers[i + 1])
    return pair

if __name__ == "__main__":
    numbers = list(map(int, input("Enter a list of numbers: ").split()))
    result = find_closest_pair(numbers)
    print(result[0], result[1])
