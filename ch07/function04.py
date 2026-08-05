def printChar(ch,n): #重複印'ch'，共印n次
  for i in range(n):
    print(f'{ch}',end='')
  print()
  
ch='A'
n1=12
printChar(ch,n1)
printChar('$',15)
printChar('B',n1+4)
