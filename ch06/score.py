no=[1,2,3,4]
score=[[87,64,88],[93,72,86],[80,88,89],[79,91,90]]
print('編號  語文  數理  智力  總分')
print('================================')
for i in range(len(no)):
  print(f'{no[i]:2d}', end='   ')
  hSum=0
  for j in range(len(score[i])):
    print(f'{score[i][j]:3d}',end='   ')
    hSum+=score[i][j]
  print(f'{hSum:3d}')
print('平均',end='  ')
for j in range(3):
  vSum=0
  for i in range(len(no)):
    vSum+=score[i][j]
  print(f'{vSum/len(no):4.1f}',end='  ')
    