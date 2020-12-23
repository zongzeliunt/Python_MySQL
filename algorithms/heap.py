def max_heap (arr, start, end):
    dad = start
    son = dad * 2 + 1
    while (son <= end):
        if son + 1 <= end and arr[son + 1] > arr[son]:
            son += 1
            #this is find the most big son from two sons
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
    mid = length // 2
    for i in range (mid, -1 , -1):
        #make the whole tree a max heap tree
        #only work on the first half, ��Ϊ������Ҷ�ӽڵ㣬��Ҷ�������󶥶�Ҳû����
        max_heap(arr, i, length)

    for i in range (length, -1 , -1):
        #list��0λ�Ǵ󶥶ѵĶ���������������Ū�����ȥ
        list_swap(arr, 0, i)
        #ʣ�µ�������һ�δ󶥶�
        max_heap(arr, 0, i - 1)
        #��һ�ְѶ��ŵ������ڶ�λ���Դ�����
    
    
def list_swap(arr, pos_0, pos_1):
    tmp = arr[pos_0]
    arr[pos_0] = arr[pos_1]
    arr[pos_1] = tmp


arr = [3,5,3,0,8, 6,1,5,8,6, 2,4,9,4,7, 0,1,8,9,7, 3,1,2,5,9, 7,4,0,2,6]
heap_sort(arr)


print (arr)


