def factorial(n):
  result = 1
  for i in range(1,n+1):
    result *= i
  return result
def main():
  while 1:
    try:
      user_input = int(input("請輸入一個大於等於1的整數n: "))
      if user_input >= 1:
        break
      else:
        print('[錯誤]輸入值必須大於等於1,請重新輸入!\n')
    except ValueError:
      print('[錯誤]輸入內容非有效整數,請重新輸入!\n')
  ans = factorial(user_input)
  print(f'\n計算結果: {user_input}! = {ans}')

if __name__ == "__main__":
  main()