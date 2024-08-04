"""task1.py"""

def InsertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

if __name__ == "__main__":
    list_a = list(map(int, input("Enter a list: ").split()))
    print(" ".join(list(map(str, InsertionSort(list_a)))))
