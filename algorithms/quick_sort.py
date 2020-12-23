
def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot_index = partition(arr, left, right)
    quick_sort(arr, left, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, right)

def partition (arr, left, right):
    pivot = left
    index = pivot + 1
    for i in range (index, right + 1):
        if arr[i] < arr[pivot]:
            list_swap (arr, i, index)
            index += 1
    list_swap(arr, pivot, index - 1)
    return index - 1


def list_swap(arr, pos_0, pos_1):
    tmp = arr[pos_0]
    arr[pos_0] = arr[pos_1]
    arr[pos_1] = tmp

arr = [3,5,3,0,8, 6,1,5,8,6, 2,4,9,4,7, 0,1,8,9,7, 3,1,2,5,9, 7,4,0,2,6]
#arr = [3,5,3,0,8]
#heap_sort(arr)

quick_sort(arr, 0, len(arr) - 1)





print (arr)
