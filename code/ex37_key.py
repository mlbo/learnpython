#-*- coding: utf-8 -*-

def fen(word):
	print "-----------*****-------------"
	print word
# del:用于list列表操作，删除一个或者连续几个元素。

# from：导入相应的模块，用import或者from...import

# as：as单独没有意思，是这样使用：with....as用来代替传统的try...finally语法的。
	# 基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
	# 紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
	# 当with后面的代码块全部被执行完之后，将调用前面，返回对象的__exit__()方法。

# global: 定义全局变量
#定义全局变量，变量名全部大写
NAME = "py"
#得到NAME值
def get_NAME():
    return NAME  
#重新设定NAME值
def set_NAME(name_value):
# 没有global则NAME值不变
    global NAME
    NAME = name_value
fen('global')
print u"输出全局变量NAME的值:", get_NAME()
new_name = "521py"
set_NAME(new_name)#为全局变量重新赋值
print u"输出赋值完的全局变量NMAE的值:", get_NAME()

# assert：表示断言（断言一个条件就是真的，如果断言出错则抛出异常）用于声明
	# 某个条件为真，如果该条件不是真的，则抛出异常：AssertionError
 
# pass：pass的意思就是什么都不做。用途及理解：当我们写一个软件的框架的时候，
	# 具体方法啊，类啊之类的都不写，等着后续工作在做。那么就在方法和类里面加
	# 上pass，那样编译起来就不会报错了！就像这样：
def test_pass():pass  
# 如果不加pass，抛出错误：IndentationError: expected an indented block
fen('pass')
test_pass()

# yield：用起来和return很像，但它返回的是一个生成器。
def test_yield(n):
    for i in range(n):
        yield i*2#每次的运算结果都返回
fen('yield')             
for j in test_yield(8):
    print j,":",
print u"结束理解yield" 

# exec：exec语句用来执行储存在字符串或者文件中的python语句。可以生成一个包
	# 含python代码的字符串，然后使用exec语句执行这些语句。

# in：查找列表中是否包含某个元素，或者字符串a是否包含字符串b。
first_list = [1, 2]
second_list = [1, 2, 3,[1, 2]]
element = 1
red = 'red'
red_clothes = "red clothes"
fen('in')
print red in red_clothes #true
print first_list in second_list  #true
print element in first_list      #true

# raise：raise可以显示地引发异常。一旦执行raise语句，后面的代码就不执行了

# is：Python中的对象包含三要素：id、type、value其中id用来唯一标识一个对象，
	# type标识对象的类型，value是对象的值is判断的是a对象是否就是b对象，
	# 是通过id来判断的 
#理解is
e = 1
es = 1.0
ess = 1
fen('is')
print u"""is就是比对id的值，看是否指向同一对象，
这里需要注意的是：同一对象,不是值相等就是同一对象。"""
print "e = es:",e == es
print id(e)
print id(es)
print id(ess)

# lambda:即匿名函数，不用想给函数起什么名字。提升了代码的简洁程度。 
g = lambda :"lambda test."
print fen('lambda')
print g()
num1 = lambda x, y=1:x + y
print num1(1)      #多个变量的时候，可以不给有默认值的变量传值
print num1(10,10)  #值得注意的是，如果y没有默认值而且不给它传值的话报错！