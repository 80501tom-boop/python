import random
dice_result=random.randint(1,6) #隨機整數
print('1.randint 案例(擲骰子):',dice_result)

even_num=random.randrange(0,10,2) #以2為間隔，0~10隨機抽一整數
print('2.randrnage 案例 (抽0~8之間的偶數):', even_num)

chance=random.random() #隨機浮點數
print('3. random 案例(機率/百分比):', chance)

temperature=random.uniform(36.0,37.5)#36.0~37.5之間的隨機浮點數
print(f'4. uniform 案例(隨機體溫):{temperature:.2f} °C')

pets=['貓咪','狗狗','兔子','倉鼠']#字串、串列等序列中隨機抽取一個元素
my_pet=random.choice(pets)
print(f'5. choice 案例(隨機選一種寵物):{my_pet}')

lottery_pool=[1,2,3,4,5,6,7,8,9,10]#從序列中隨機抽取不重複的元素
winning_numbers=random.sample(lottery_pool,3)
print(f'6. sample 案例(抽3個不重複的樂透號碼):{winning_numbers}')

poker_cards=['A','K','Q','J','10']
random.shuffle(poker_cards)#將序列中的元素隨機排序(無回傳值，會修改原串列)
print(f'7. shuffle 案例(洗牌後的順序):{poker_cards}')