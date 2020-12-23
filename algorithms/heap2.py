
def max_heap_2 (arr, dad, end):
    if dad * 2 + 1 > end or dad * 2 + 2 > end:
        #make sure all sons in range
        return
    son = dad * 2 + 1
    if son + 1 < end and arr[son+1] > arr[son]:
        #find biggest son in two sons
        son += 1
    if arr[dad] > arr[son]:
        #dad is bigger than two sons
        return
    else:
        #dad is smaller than son, make son to heap
        #dad swap to son position, make this sub tree max heap tree
        list_swap (arr, dad, son)
        dad = son
        max_heap_2(arr, dad, end)

def heap_sort (arr):
    length = len(arr) - 1
    mid = length // 2
    for i in range (mid, -1, -1):
        #make the whole tree a max heap tree
        #only work on the first half, 因为后半段是叶子节点，在叶子上做大顶堆也没意义
        max_heap_2(arr, i, length)

    for i in range (length, -1, -1):
        #list的0位是大顶堆的顶，所有数里的最大，弄到最后去
        list_swap(arr, 0, i)
        #剩下的数再做一次大顶堆
        max_heap_2(arr, 0, i - 1)
        #下一轮把顶放到倒数第二位，以此类推

def list_swap(arr, pos_0, pos_1):
    tmp = arr[pos_0]
    arr[pos_0] = arr[pos_1]
    arr[pos_1] = tmp


arr = [3,5,3,0,8, 6,1,5,8,6, 2,4,9,4,7, 0,1,8,9,7, 3,1,2,5,9, 7,4,0,2,6]
heap_sort(arr)


print (arr)

