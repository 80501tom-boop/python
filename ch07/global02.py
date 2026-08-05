def subpro():
  global n
  n+=10
  m=20
  print('---- subpro ----')
  print(f'n = {n},m = {m}')

n=100
m=200
print('---- main ----')
print(f'n = {n},m = {m}')

subpro()
print('---- main ----')
print(f'n = {n},m = {m}')

subpro()
print('---- main ----')
print(f'n = {n},m = {m}')