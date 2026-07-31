lst1=[10,20,30,40,50]
print(f'0. 初始狀態:{lst1}\n'+'-'*40)

lst1.append(66)
print(f'1. append(66) 後 :{lst1}')

lst1.insert(2,77)
print(f'2. insert(2,77) 後 :{lst1}')

cnt=lst1.count(30)
idx=lst1.index(30)
print(f'3. 數字 30 出現{cnt}次,地位於索引:{idx}')

lst1.remove(20)
print(f'4. remve(20) 後 :{lst1}')

remved_val=lst1.pop(3)
print(f'5. pop(3)移除了[{remved_val}],剩餘:{lst1}')

lst1.pop()
print(f'6. pop() 後:{lst1}')
print("\n" + '=' * 40 + '\n[測試del切片與clear方法]\n')

lst2=[11,22,33,44,55,66,77]
print(f'原始 lst2:{lst2}')
del lst2[1:5:2]
print(f'del lst2[1:5:2] 後:{lst2}')

lst2.clear()
print(f'lst2.clear() 後 : {lst2}')