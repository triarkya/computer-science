from random import randint


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j >= 1 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def merge_sort(arr):
    arr_list = [[elem] for elem in arr]
    arr_list_copy = []
    while True:
        for i in range(0, len(arr) - 1, 2):
            try:
                arr_a = arr_list[i]
            except IndexError:
                arr_a = []
            try:
                arr_b = arr_list[i + 1]
            except IndexError:
                arr_b = []
            if len(arr_a) == len(arr) and 0 == len(arr_b):
                return arr_a
            chunk = []
            while len(arr_a) > 0 and len(arr_b) > 0:
                if arr_a[0] < arr_b[0]:
                    chunk.append(arr_a[0])
                    del arr_a[0]
                else:
                    chunk.append(arr_b[0])
                    del arr_b[0]
            if len(arr_a) == 0:
                chunk.extend(arr_b)
                del arr_b
            elif len(arr_b) == 0:
                chunk.extend(arr_a)
                del arr_a
            arr_list_copy.append(chunk)
        arr_list = arr_list_copy


if __name__ == '__main__':
    liste_a = [randint(0, 50) for _ in range(12)]
    print(liste_a)
    print("insertion sort:", insertion_sort(liste_a))
    liste_b = [randint(0, 100) for _ in range(30)]
    print(liste_b)
    print("merge sort:", merge_sort(liste_b))
