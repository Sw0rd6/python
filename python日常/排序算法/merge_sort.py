#归并排序：采用分治法的思想，先递归分解再合并数组。
def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    num = int(len(ls) / 2)
    left = merge_sort(ls[:num])     #归并排序精髓所在，递归分解序列
    right = merge_sort(ls[num:])    ＃归并排序精髓所在，递归分解序列
    return merge(left, right)
def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
