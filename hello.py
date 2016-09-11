#-*-coding:utf-8-*-
height=1.75
weight=80.5
bmi=weight/height/height
if bmi<18.5:
    print("too light")
elif bmi <23:
    print("normal")
elif bmi<28:
    print("a bit heavy")
elif bmi<32:
    print("obesity")
else:
    print("too heavy")
print('中文'.encode('utf-8'))