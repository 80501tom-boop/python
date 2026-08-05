import random as R
max=35
min=18
num=6
arr=[0 for x in range(num)]
n=0
while (n<num):
  isRepeat=False
  rnd=R.randint(min,max)
  for v in arr:
    if rnd==v:
      isRepeat=True
      break
  if not isRepeat:
    arr[n]=rnd
    n+=1

for i in range(num):
  print(f'第{i+1}個亂數:{arr[i]}')