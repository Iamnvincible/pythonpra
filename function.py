import math
print(abs(-345))
print(int('3445'))
print(hex(65535))
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if(x>=0):
        return x
    else:
        return -x
x=my_abs(-4545)
print(x)
if(334):
    pass

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)

def quadratic(a,b,c):
    det=math.pow(b,2)-4*a*c
    if det<0:
        return None
    elif det==0:
        result = ((-b)+math.sqrt(det))/2
        return result,result
    else:
        return ((-b)+math.sqrt(det))/2,((-b)-math.sqrt(det))/2
x1,x2=quadratic(1,2,1)
print(x1,x2)
#默认参数
def add_end(L=None):
    if(L is None):
        L=[]
    L.append('End')
    return L
print(add_end())
print(add_end())
#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum+=n*n
    return sum
print(calc(3,3))
t=[1,2,3]
print(calc(*t))

#关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Michae',30)
person('Bob',34,city='Beijing')
person('Adma',44,city='Beijing',job="Engineer")
extra={"city":"Beijing",'job':'Engineer'}
person('Jack',34,**extra)


#命名关键字参数
def person2(name,age,*,city,job='Teacher'):
    print(name,age,city,job)
person2('Jack',23,city='Beijing',job='Engineer')
person2('Jack',44,city='Nanjing')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,3)
f1(1,2,c=4)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

args=(1,2,3,4)
args2=(1,2,3)
kw={'d':99,'x':'#'}
f1(*args,**kw)
f2(*args2,**kw)


# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。