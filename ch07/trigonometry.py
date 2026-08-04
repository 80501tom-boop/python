import math
a_d=30
h=10.0
r=a_d*(math.pi/180)
height=h*math.sin(r)
print(f'30度角、斜邊長10時的高度為:{height:.2f}')
tan_value=1.0
rad_result=math.atan(tan_value)
deg_result=rad_result*(180/math.pi)
print(f'tan答案為1時的角度為:{deg_result:.1f}度')