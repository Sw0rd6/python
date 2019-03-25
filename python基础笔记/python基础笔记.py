python基础笔记
Python计算生态 = 标准库 +第三方库

开篇turtle画图工具

turtle.setup(width,height,startx,starty)
Setup不是必备项

turtle.penup() 别名turtle.pu()
画笔起飞

turtle.pendown() 别名turtle.pd()
画笔降落

turtle.pensize(d)
画笔宽度d

turtle.pencolor(color)
画笔颜色
color可以是颜色名字的字符串，比如"purple"
turtle.pencolor("purple")
turtle.pencolor(0.63,0.13,0.94)
turtle.pencolor((0.63,0.13,0.94))

turtle.goto(x,y)两点之间画线

turtle.circle(x,y)
x代表半径，y代表要走的弧长，y不写默认画圆
x为正说明圆心在前进方向的左边，负则右
circle()函数也可以自定义（一个圆是由长度相同的直线以一定角度拼接而成）
import turtle as t
def circle(x, y, r):
    n = 40
    angle = 360 / n
    pi = 3.1415926
    c = 2 * pi * r
    l = c / n
    start_x = x + l / 2
    start_y = y + r
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    for i in range(n):
        t.fd(l)
        t.right(angle)
    t.done()
circle(0, 0, 300)

以上是大致的自定义circle()函数

turtle.bk(d)
往回走d的距离

turtle.fd(d)
前进d的距离 fd即为forward

turtle.seth(angle)     全称是setheading
这个操作不会画线，只改变海龟朝向

turtle.left(d)
左转d度

turtle.right(d)
右转d度

RGB色彩模式
turtle.colormode(mode)
若mode等于1.0则RGB选择小数
mode=255则选择整数来定义色彩

常见的色彩查表用即可

库引用方法三种，用最好用的就是第一种
import turtle as t
turtle.setup()

imoprt turtle
t.setup()

from turtle import 函数名
from turtle import *
setup()

以上看似第三种最简洁，然而第三种有和自定义函数冲突的风险，不宜采用
----------------------------------------------------------------------------------
time库时间工具库
time.time()
获得的当前时间戳，浮点数

time.ctime()
易读方式的字符串

time.gmtime()
获得当前时间，表示为计算机可处理方式

t.time.gmtime()
time.strftime(“%Y-%m-%d %H-%M-%S”,t)
%Y年份，%m月份，%d日期，%H时，%M分钟，%S秒

time.strptime()
与上相反

time.sleep()
程序休眠

time.perf_counter()
end-start(设两个点相减)
---------------------------------------------------------------------
python常用库random库
import random    
random.seed(a)
初始化给定的种子，默认为当前系统时间

random.random()
生成一个[0.0,1.0]之间的随机小数

random.randint(a,b)
生成一个[a,b]之间的整数

random.getrandbits()
生成一个k比特长的随机整数

random.uniform(a,b)
生成一个[a,b]之间的随机小数

random.randrange(m,n[,k])
生成一个[m,n)之间以k为步长的随机整数，前包后不包

random.choice(ls)
从序列ls中随机选择一个元素

random.sample(ls,k)
从指定序列中随机获取k个元素作为一个片段返回，sample函数不会修改原有序列

random.shuffle(ls)
将序列元素随机排列，返回打乱后的序列

random.triangular(low,high,mode)
返回三角形分布的随机数，low,high为上下限,mode为中值

random.betavariate(alpha,beta)
beta分布的随机数
----------------------------------------------------------------------


python第一部分 数据类型&字符串操作
整数int
浮点数float
比较时用round(x,d)
d为小数点后位数

复数
z=1.23e-4+5.6e+89j
z.real获得实部
z.imag获得虚部

常见计算函数写下
abs()算绝对值

divmod()是两个运算结合
x//y和x%y

pow()幂运算

max()
min()等等

字符串：
索引、切片比较熟悉，在此省略……

字符串部分处理函数（容易混淆的两个）
chr(x):x为Unicode编码，返回字符

ord(x)：x为字符，返回Unicode编码

字符串处理方法：
str.lower()

str.upper()

str.split(""):返回一个列表，字符串转列表的方法

ls = [] , str = "".join(ls) :列表转字符串的方法

str.count(sub):返回字符串sub在str中出现的次数

str.replace(old,new)

str.center(width,"")：字符串str根据宽度width居中，后面为补上的东西

str.strip(chars)：从str去掉左右侧chars列出的字符
"= python= ".strip(" =np")结果是"ytho"

str.join(",")：在每个字符后面加""里面的内容，用于分隔

字符串格式化：
"".format()格式："{参数序号:格式化控制标记}"
槽内部对格式化的配置方式：
:(填充字符)(对齐方式)(宽度)(千分位)(精度)(数据类型)
举例：{0：*^20}.format("python") 结果是"*******python*******"
          {0:,.2f}.format(12345.)

字符串操作更多内容：
１．转义字符和原始字符串：
转义字符是\，而重点说说原始字符串：
在字符串开始的引导之前加上r，print(r'this is xx\'s cat.')

而没有r的话会导致报错，报错原因就是‘s这一部分，系统把他识别处和前面一处的单引号结束了，而后面的单引号不知何去何从。
正确操作就是加入\,让系统辨别出's并不是结束，这就是转义字符起到的作用。
之后正则表达式也挺重要。
     
添加几个字符串方法：
is系列的
islower()
isupper()   这两个呢，如果字符串至少有一个字母，且所有字母都是大/小写，返回True，否则False
字符串有数字和字母，但字母都是大写或者消小写，他还是会True
     
isalpha()   只含字母，并且非空，True
isalnum()   只含字母和数字，并且非空, True
isdecimal() 只含数字，并且非空，返回True
isspace()   
istitle()
split("\n")是一个常见的用法，可以分隔多行字符串
import pyperclip
copy()和paste()

--------------------------------------------------------------------------------------------

python第二部分 分支结构
补个异常处理:
try:
    ……
except:
    print()

python第三部分： 循环结构
    
遍历：
for …… in ……

无限循环：
while:
    
-----------------------------------------------------------------------------
python第三部分： 函数
主要是参数传递的内容吧：
def <函数名>（<非可选参数>，<可选参数>）：
    可选参数传递例如：
def <>(n,m=1)
    可变参数传递例如：
def <>(<参数>,*b)
    就是后面可以有多个参数，在调用时可能是<>(n,1,2,3)

传递方式有位置传递和名称传递

返回值可以多个

局部变量和全局变量
举个栗子更直接：
     n,s=10,100     ---------------def 上的全局变量
     def fact(n):    -- ----------局部变量
        s=1          ------------局部变量
print(fact(n),s) ------------全局变量

规则：
1.局部变量和全局变量是不同变量
函数内部使用全局变量则是用global定义

2.局部变量为组合数据类型且未创建，等同于全局变量

lambda函数：这个函数之前一直不太会用,但却又被建议少用
返回函数名作为结果
<函数名> = lambda <参数>:<表达式>
举例：x = lambda x,y:x+y
f = lambda:”lambda函数“     print(f())

函数的递归：
类似数学归纳法，递归是数学归纳法思维的编程体现
举例说明：
def f(n):
    ……
    return f(n-1)*n (假设)

函数递归实例解析：
1.字符串反转：
def rvs(s):
    if s == "" :
          return s 
     else:
          return rvs(s[1:])+s[0]
虽说字符串反转只要s[::-1]。。。

2.斐波那契数列：
def f(n):
     if n == 1 or n == 2:
          return 1
     else:    
          return f(n-1)+f(n-2)
(经典的函数递归案例) 

3.汉诺塔～（最初的诺基亚小游戏）
函数+分支结构
递归链条
（推导还是有点难度的），已推过，如图。


------------------------------------------------------------
Python库之Pyinstaller

pyinstaller -i xxx.ico -F xxx.py
生成有图标的可执行文件

python第四部分 组合数据类型
1.集合类型
集合元素不可更改
集合处理方法
S.add()
添加元素

S.discard()
移除元素，没有该元素不报错

S.remove()
移除元素，元素不在的话，返回keyerror异常

S.clear()
清除所有元素

S.pop()
随机返回s的一个元素，更新s，若没有会返回keyerror 

S.copy()

set(x)
将其他类型变量转换为集合类型

数据去重
对有重复数据的数据类型用set(x)就能解决了
比如对列表里面的重复数据去重
python第五部分 序列类型
序列的部分通用函数温习
s.index(x)
或者s.index(x,i,j)
就是返回序列中第一次出现x元素的位置，或者是i到j的范围内第一次出现的位置

元组类型
不可修改，用()表示或者tuple()表示
没什么多余操作
列表类型
可扩展，常用
ls.append(i)
增加元素

ls.clear()
清除元素

ls.copy()
复制元素

ls.insert(i,x)
在i的位置插入x

ls.pop(i)
将位置i的元素取出并删除

ls.remove(x)
将列表中第一个出现的x元素删除

ls.reverse()
将列表元素反转

列表数据保护，可将列表转换为元组
ls = []
lt = tuple(ls)
python第六部分 字典类型
键值对构成字典
d = {}
[]用来对字典索引和增加元素

del d[k]
删除k键对应的值

d.keys()
返回所有的键

d.values()
返回所有的值

d.items()
返回所有的键值对

d.get(k,default)  常用
键存在就返回相应值

d.pop(k,default)
同上

d.popitem()
随机从字典d中取出一个键值对，以元组形式返回

d.clear()
删除所有的键值对
python库之jieba库
中文分词第三方库

jieba分词三种模式
精确模式
jieba.lcut(s)
返回一个列表类型分词结果
精确切分，不存在冗余

全模式
jieba.lcut(s,cut_all=True)
有冗余，但较详细

搜索引擎模式
jieba.lcut_for_search(s)
精确模式基础上，在进行切分
jieba.add_word(w)
向分词词典新增w词语

---------------------------------------------
python第七部分 文件操作
文本文件：由单一特定编码组成的文件（如utf-8编码）
二进制文件：没有统一字符编码
文件处理的步骤：
打开-操作-关闭
a.open()
文件的打开：open(文件名，打开模式)
打开模式：
‘r’只读模式
‘w’覆盖写模式
'x'创建写模式
'a'追加写模式
‘b’二进制文件模式
‘t’文本文件模式
‘+’与rwxa一同使用，原有基础上增加读写功能

a.close()

a.read(size)

a.readline(size)

a.readlines(hint)

a.write(s)

a.writelines(lines)

a.seek(offset)
offset分为0,1,2
0为文件开头，1为当前位置，2为文件结尾

一维数组的读入
txt = open(fname).read()
ls = txt.split()
一维数组的写入
ls = [……]
open(fname,'w')
f.write(' '.join(ls))

二维数组
二维数组的存储
二维数据的读入，写入，逐行处理
-------------------------------------------------------------
python库的wordcloud库
优秀的词云展示第三方库

------------------------------------------------------------
python第八部分 计算生态
多方应用库，具体做哪个方向自然熟练很多库，这里就不细说。
