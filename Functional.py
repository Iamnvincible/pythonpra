from functools import reduce
import functools
import math
#Higher-order function高阶函数
def fun(m,n,f):
    return f(m)+f(n)
x=fun(2,3,abs)
print(x)

def f(x):
    return x*x
r=map(f,[1,2,3,4,5,5])
print(list(r))
s=list(map(str,[1,2,3,4,5,6,7]))
print(s)
def add(x,y):
    return x+y
sum=reduce(add,[1,3,5,7,9])
print(sum)

def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

stri=reduce(fn,map(char2num,'123456'))
print((stri))

def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
stri=str2int('3445566')
print(stri)

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def Upper(s):
    return s.title()
L1=['adam','LISA','barT']
name=(map(Upper,L1))
print(list(name))

#Python提供的sum()函数可以接受一个list并求和，===请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y:x*y,L)
L1=[1,2,3,4,5]
print(prod(L1))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def fm(x,y):
    return x*+y*0.1
def str2float(s):
    z,x=s.split('.')
    a=reduce(fn,map(char2num,z))
    b=reduce(fn,map(char2num,x))
    return a+b/math.pow(10,len(x))
print(str2float('3435432.14453636535'))

#filter
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8])))
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,["A","B",None,"c",''])))

def odd_iter():
    n=1
    while True:
        n+=2
        yield n
def not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(not_divisible(n),it)

for n in primes():
    if(n<30):
        print(n)
    else:
        break

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：

def numb(n):
    return str(n)==str(n)[::-1]

def samenumb():
    return filter(lambda x:str(x)==str(x)[::-1],range(1000))
print(list(samenumb()))


#sorted
print(sorted([1,2,4,6,0,-213,-45,456,3425,2345,-134,56,13,784]))
print(sorted([1,2,4,6,0,-213,-45,456,3425,2345,-134,56,13,784],key=abs))
print(sorted([1,2,4,6,0,-213,-45,456,3425,2345,-134,56,13,784],key=abs,reverse=True))
print(sorted(['kdg','KDGhg','anbgF','Kdfjg','erdaf'],key=str.lower))

#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=lambda x:x[0]))
print(sorted(L,key=lambda x:x[1]))

#返回函数
#一个函数可以返回一个计算结果，也可以返回一个函数。
#返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

def lazy_sum(*agrs):
    def sum():
        ax=0
        for n in agrs:
            ax+=n
        return ax
    return sum
sumfun=lazy_sum(1,2,3,4,5,6,7,8,9)
print(sumfun())

#闭包

def count():
    fs=[]
    for i in  range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1(),f2(),f3())

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
f11,f12,f13=count2()
print(f11(),f12(),f13())

#匿名函数
#就是lambda表达式
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7])))

#装饰器 decorator,在运行时添加功能
#函数也是对象，可以赋值给变量
def now():
    print('2016-9-15')
d=now
d()
print(now.__name__)

def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
#我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now2():
    print('2016-9-15')
now2()

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now3():
    print('2015-3-25')
now3()
print(now3.__name__)
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
        
@log('exe')
def now():
    print('20000')
now()
print(now.__name__)

#编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#再思考一下能否写出一个@log的decorator，使它既支持
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        x= func(*args,**kw)
        print('end call %s():'%func.__name__)
        return x
    return wrapper
@log
def now():
    print('20000')
now()
print(now.__name__)

def log(txt):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin call: log%s(%s)' % ('' if callable(txt) else "('%s')" % txt, func.__name__))
            x= func(*args,**kw)
            print("end call")
            return x
        return wrapper
    return decorator(txt) if callable(txt) else decorator
@log('你好')
def now():
    print('20000')
now()
print(now.__name__)

#偏函数Partial function
print(int('2334', base=16))

int2=functools.partial(int,base=2)
print(int2('1111111'))
max2=functools.partial(max,10)
print(max2(1,2,3,4,4))