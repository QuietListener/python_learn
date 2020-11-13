'''
import语句允许在当前运行的程序文件中使用模块中的代码
'''

import pizza
import pizza as pz #别名

pizza.make_pizza("a","b")
pz.make_pizza("c","d")
