#堆排序：三步曲走：１．构造最大堆２．堆排序３．最大堆调整
def heap_sort(ls):
    n = len(ls)
    #first为最后一个非叶子节点开始往前扫描
    first = int(len(ls) / 2 - 1)
    ＃构造最大堆
    for i in range(first, -1, -1):
        max_heapify(ls, i, n - 1)
    ＃最大堆的调整
    for end in range(n - 1, 0, -1):
        ls[end], ls[0] = ls[0], ls[end]
        max_heapify(ls, 0, end - 1)
    return ls
def max_heapify(ls, start, end):
    root = start
    while True:
        child = root * 2 + 1    ＃保证整个二叉堆都进行完整的比较，保证每次交换的节点和剩下的子节点相比都是最大的或者最小的。
        if child > end:
            break
        ＃兄弟节点的比较
        if child + 1 <= end and ls[child] < ls[child + 1]:
            child = child + 1
        if ls[root] < ls[child]:
            ls[root], ls[child] = ls[child], ls[root]
            root = child
        else:
            break
