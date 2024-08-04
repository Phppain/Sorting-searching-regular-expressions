"""task6.py"""

def adjust_array(arr):
    pos_sum = sum(x for x in arr if x > 0)
    neg_sum = sum(x for x in arr if x < 0)
    new_element = abs(neg_sum) - pos_sum
    arr.append(new_element)
    return arr, new_element

if __name__ == "__main__":
    arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
    adjusted_arr, new_element = adjust_array(arr)
    print(adjusted_arr)
    print(new_element)
