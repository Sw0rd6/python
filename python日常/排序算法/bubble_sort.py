#冒泡排序法:通过两两比较，每次都把最大或者最小的数往下沉，而把后面的往上浮，通过不断的缩小比较的长度来达到排序的目的。
＃python实现
def bubble_sort():
	#设给定一个序列为ls
	n = len(ls)
	for i in range(n):	
		for j in range(1, n - i):	#n - i是冒泡的精髓
    		if ls[j - 1] > ls[j]:
        		ls[j - 1], ls[j] = ls[j], ls[j - 1]
return ls
