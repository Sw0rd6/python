#插入排序：构建有序序列，序列第一个元素被视为已排序，后续的就通过对已排序的序列进行从后到前的扫描，在相应的位置插入即可
#设给定的序列为ls
def insert_sort():
	n = len(ls)
	for i in range(1, n):
		if ls[i - 1] > ls[i]:
			temp = ls[i]	#使用临时空杯存放ls[i]
			index = i			#index记录下标
			for j in range(i - 1, -1 , -1):		#插入排序的重点就在于这个循环的参数，所谓的从后往前扫描 -> (i - 1, -1, -1)
				if ls[j] > temp:
					ls[j + 1], ls[j] = ls[j], ls[j + 1]
					index = j
				else:
					break
			#ls[index] = temp
	return ls
