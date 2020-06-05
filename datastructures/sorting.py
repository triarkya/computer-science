from collections import defaultdict
from random import randint


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j >= 1 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def bubble_sort(arr):
    last_pos = len(arr) - 1
    while last_pos > 0:
        for i in range(last_pos):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            if i + 1 == last_pos:
                last_pos -= 1
    return arr


def counting_sort(arr):
    sorted_arr = len(arr) * [0]
    index_dict = defaultdict(int)
    # count each element
    for elem in arr:
        index_dict[elem] += 1
    # set the index array
    index_arr = (max(index_dict.keys()) + 1) * [0]
    for k, v in index_dict.items():
        index_arr[k] += v
    for i in range(1, len(index_arr)):
        index_arr[i] += index_arr[i-1]
    # start sorting
    for elem in arr:
        sorted_arr[index_arr[elem] - 1] = elem
        index_arr[elem] -= 1
    return sorted_arr


def heap_sort(arr):
    # build heap
    for i in range(int(len(arr) / 2) - 1, 0, -1):
        # heapify
        pos = i
        pos_next = 2 * i + 1
        while pos_next < len(arr):
            if pos_next + 1 < len(arr) and arr[pos_next + 1] > arr[pos_next]:
                pos_next += 1
            if arr[pos] >= arr[pos_next]:
                break
            arr[pos], arr[pos_next] = arr[pos_next], arr[pos]
            pos = pos_next
            pos_next = 2 * pos + 1
    for j in range(len(arr) - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        pos = 0
        pos_next = 1
        # heapify
        while pos_next < j:
            if pos_next + 1 < j and arr[pos_next + 1] > arr[pos_next]:
                pos_next += 1
            if arr[pos] >= arr[pos_next]:
                break
            arr[pos], arr[pos_next] = arr[pos_next], arr[pos]
            pos = pos_next
            pos_next = 2 * pos + 1
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
    liste_a = [randint(0, 1000) for _ in range(300)]

    print("insertion sort:", insertion_sort(liste_a.copy()))
    print("bubble sort: ", bubble_sort(liste_a.copy()))
    print("counting sort: ", counting_sort(liste_a.copy()))
    print("heap sort: ", heap_sort(liste_a.copy()))
    print("merge sort:", merge_sort(liste_a.copy()))
