def triangle(B=6,H=6):
  print()
  print(f'三角形的底為 {B} 高為 {H}')
  A=B*H/2
  return A
base=10
high=5
area1=triangle(base,high)
print(f'三角形的面積為:{area1}')
area2=triangle(base)
print(f'三角形的面積為:{area2}')
area3=triangle()
print(f'三角形的面積為:{area3}')