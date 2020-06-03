def binary_search(element, arr):
    left_pos = 0
    right_pos = len(arr) - 1
    while left_pos <= right_pos:
        middle_pos = int((left_pos + right_pos) / 2)
        if arr[middle_pos] < element:
            left_pos = middle_pos + 1
        elif arr[middle_pos] > element:
            right_pos = middle_pos - 1
        elif arr[middle_pos] == element:
            return True
    return False


if __name__ == '__main__':
    print(binary_search(6, [1, 2, 3, 5, 6, 8]))