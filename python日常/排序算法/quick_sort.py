‘’‘
快速排序：设基准数（以第一个数为基准的话），从左到右比较，直到出现比基准大的数，返回那个位置index；
从右到左，如果比基准数小的话，先与index交换，直到左右index（也就是lp == rp），原地交换后，把这个数和第一次的基准数交换；
接下来就对左右的子数组用同样的方式排序。
‘’‘
#快速排序使用递归实现
def quick_sort(ls):
    return qsort(ls, 0, len(ls) - 1)
def qsort(ls, left, right):
    if left >= right:
        return ls
    key = ls[left]
    lp = left
    rp = right
    while lp < rp:
        while ls[rp] >= key and lp <rp:
            rp -= 1
        while ls[lp] <= key and lp < rp:
            lp += 1
        ls[lp], ls[rp] = ls[rp], ls[lp]
    ls[left], ls[lp] = ls[lp], ls[left]
    qsort(ls, left, lp - 1)
    qsort(ls, rp + 1, right)
    return ls
