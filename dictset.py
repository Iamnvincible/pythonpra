#dict元素字典
d={'Michael':95,'Bob':75,'Tracy':85}
d['Michael']=44
print(d['Michael'])
print('Tomas' in d)
print(d.get('Tomas'))
print(d.get('Tomas'),-233)

#set 元素不能重复
s=set([1,2,3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
s2=set([2,3,4,5])
print(s & s2)
print(s | s2)

