def max_heap (arr, start, end):
    dad = start
    son = dad * 2 + 1
    while (son <= end):
        if son + 1 <= end and arr[son + 1] > arr[son]:
            son += 1
            #this is find the most big son
        if arr[son] < arr[dad]:
            #dad is bigger than two son
            return
        else:
            #swap dad and son
            #start from son to create big heap
            list_swap(arr, dad, son)
            dad = son
            son = son * 2 + 1

def heap_sort(arr):
    length = len(arr) - 1
    mid = length / 2
    for i in range (mid, -1 , -1):
        max_heap(arr, i, length)

    for i in range (length, -1 , -1):
        list_swap(arr, 0, i)
        max_heap(arr, 0, i - 1)
    
    
def quick_sort (arr, start, end):
    if start >= end: 
        return
    base = arr[end]
    left = start
    right = end - 1
    while (left < right):
        while arr[right] >= base:
            right = right - 1
        while arr[left] < base:
            left = left + 1
        list_swap (arr, right, left)
    if (arr[left] >= arr[end]): 
        list_swap (arr, left, end)
    else:
        left = left + 1
    quick_sort (arr, start, left - 1)
    quick_sort (arr, left + 1, end)





    
def list_swap(arr, pos_0, pos_1):
    tmp = arr[pos_0]
    arr[pos_0] = arr[pos_1]
    arr[pos_1] = tmp


arr = [3,5,3,0,8, 6,1,5,8,6, 2,4,9,4,7, 0,1,8,9,7, 3,1,2,5,9, 7,4,0,2,6]
#heap_sort(arr)

quick_sort(arr, 0, len(arr) - 1)





print arr


