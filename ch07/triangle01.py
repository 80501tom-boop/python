def triangle(B=9,H=8):
  A=B*H/2
  return A

base=10
height=5
area=triangle(base,height)
print(f'底為 {base} 高為 {height} 的三角形面積為:{area}')
area=triangle() #使用預設值
print(f'底為 {base} 高為 {height} 的三角形面積為:{area}')