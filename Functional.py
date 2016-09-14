from functools import reduce
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
    if(n<100):
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