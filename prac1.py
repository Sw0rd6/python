#字母转数字 python写法
def change():
	d = {"2":['a','A','b','B','c','C'],
	     "3":['d','D','e','E','f','F'],
	     "4":['g','G','h','H','i','I'],
	     "5":['j','J','k','K','l','L'],
	     "6":['m','M','n','N','o','O'],
	     "7":['p','P','q','Q','r','R','s','S'],
	     "8":['t','T','u','U','v','V'],
	     "9":['w','W','x','X','y','Y','z','Z']}	#模拟手机九宫格键盘字母
	ls = []	
	s = input("请输入一段字符：")
	for j in s:
		for k in d.keys():
			if j in d[k]:
				ls.append(k)
			else:
				continue
	print(int("".join(ls)))		  
change()
