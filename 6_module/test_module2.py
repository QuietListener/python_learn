'''
import语句允许在当前运行的程序文件中使用模块中的代码
'''

from pizza import make_pizza
from pizza import make_pizza as mp #重命名

make_pizza("a","b")
mp("c","d")