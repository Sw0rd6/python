#选择排序法：每次选出序列中的最小或者最大元素，存放到排序序列的相应位置，直到未排序序列长度为０
#要注意的点就是在选定最值的时候，必须先确定min或者max的下标之后，再进行交换，才能确保是最值。
#假设给定序列为ls
def select_sort():
	n = len(ls)
	for i in range(n):
		min = i
		for j in range(i + 1, n):
			if ls[j] < ls[min]:
				min = j
		ls[i], ls[min] = ls[min], ls[i]
	return ls
				
