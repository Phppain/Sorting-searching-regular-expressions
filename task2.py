"""task2.py"""

def SelectionSort(A):
    for i in range(len(A)):
        max_idx = i
        for j in range(i + 1, len(A)):
            if A[j] > A[max_idx]:
                max_idx = j
        A[i], A[max_idx] = A[max_idx], A[i]
    return A

if __name__ == "__main__":
    list_a = list(map(int, input("Enter a list: ").split()))
    print(" ".join(list(map(str, SelectionSort(list_a)))))
