x=5
y=x
print(id(x),id(y))#顯示x,y記憶體位置
x=3+y
print(id(x))
a,b=2,3
print(id(a),id(b))
a,b=b,a #a,b變數值交換
print(id(a),id(b))