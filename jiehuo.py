#探寻__str__ 与__call__的区别
'''
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('调用__call__')

    def __str__(self):
        return 'qqq'

s=Student('sss')
s()
print(s)
'''
# 函数可变参数与关键字参数传参
def add(*wq):
    sum=0
    for i in wq:
        sum=sum+i
    print(sum)
    print (wq)
#传入的参数默认都为元组
#a=[2,3,4]
#add([1,2,3,4,5],[21])




def add1(a,b):
    print(a+b)
#传参的时候可以利用可变参数的特性封装列表或元组来传参
#a=[2,3]
#add1(*a)

def wqwq(**extra):
    print (extra)
dic1={'a':1,'b':2}
wqwq(**dic1)


