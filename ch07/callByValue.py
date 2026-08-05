def Triple(x,y):
  x=x*3
  y=y*3
  print('執行 Triple() 函式 -----')
  print(f'x={x}    y={y}')
  print()
x=10
A=[2,4,6,8]
print('呼叫 Triple() 函式前 -----')
print(f'x={x}    A[1]= {A[1]}')
print()
Triple(x,A[1])
print('呼叫 Triple() 函式後 -----')
print(f'x={x}    A[1]= {A[1]}')