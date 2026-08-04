scores = [12.5,11.5,13.5,14.5,14.51]
rounded_scores = [round(score) for score in scores]
#「五成雙」只適用於剛好等於 5 的情況。如果 5 的後面還有數字（例如 14.51），這在數學上整體大於 0.5，就會直接歸類到「大於 5 ➔ 進位」的規則，變成 3
# 14.51 -> 15
print(rounded_scores)
num=round(12.365,1)#12.4
num=round(12.367,1)#12.37
num=round(12.364,1)#12.36

print(round(12.325,2))#12.32
print(round(12.335,2))#12.34