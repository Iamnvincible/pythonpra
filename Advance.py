from collections import Iterable
from collections import Iterator
import os
#slice 切片
L=['Michael','Sarah','Tracy','Bob','Jack']
T=list(range(100))
print(L[1:3])
print(L[-2:-1])
L=list(range(100))
print(L[:-10])
print(L[10:30])
print(L[10:30:3])
print(L[::11])
print(T[::13])
print('Microsoft Lumia'[0:9])
#iteration 迭代
#for作用于可迭代对象
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
print(isinstance('abc',Iterable))
for i,value in enumerate(['A','B','C']):
    print(i,value)
for x,y in[(1,2),(2,4),(3,8)]:
    print(x,y)


#list comprehensions 列表生成
li=list(range(1,33))
limu=[x * x for x in range(1,11)]
print(li)
print(limu)
liAC=[m+n for m in 'ABC' for n in 'XYZ']
print(liAC)
lifilter=[x*x for x in range(1,11) if x%2==0]
print(lifilter)
fileanddir=[d for d in os.listdir('.')]#列出文件和目录
print(fileanddir)
for k,v in d.items():
    print(k,'=',v)
D={'x':'A','y':'B','z':'C'}
iterlist=[k+':'+v for k,v in D.items()]
print(iterlist)
L=['Hello','World','IBM','Microsoft']
Llower=[s.lower() for s in L]
print(Llower)
L.append(18)
L2=[s.lower() for s in L if isinstance(s,str)]
print(L2)


#生成器 Generator
#使用（） 而非[]
g=(x*x for x in range(10))
next(g)
for n in g:
    print(n)

    #斐波那契
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
fib(5)
def fibgenerator(max):
    n,a,b=0,0,1
    while n<max:
        yield b#yield关键字 使成为generator
        a,b=b,a+b
        n=n+1
    return 'done'
#f=fibgenerator(6)
for n in fibgenerator(6):
    print(n)
n=10
def triangles():
    L=[1]
    while len(L)<n:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]

for m in triangles():
    print(m)

#迭代器 Iterator
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance('abcd',Iterable))
print(isinstance('abcd',Iterator))
print(isinstance(iter('abcd'),Iterator))

for x in [1,2,3,4,5]:
    pass

#等价于

it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
    except StopIteration:
        break
