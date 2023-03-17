Timur = input()
Ruslan = input()
loser_r = ['ножницы', 'ящерица']
loser_p = ['камень', 'Спок']
loser_sc = ['бумага', 'ящерица']
loser_l = ['Спок', 'бумага']
loser_sp = ['ножницы', 'камень']
if Timur == Ruslan:
    print('ничья')
elif Timur == 'камень' and Ruslan in loser_r:
    print('Тимур')
elif Timur == 'бумага' and Ruslan in loser_p:
    print('Тимур')
elif Timur == 'ножницы' and Ruslan in loser_sc:
    print('Тимур')
elif Timur == 'ящерица' and Ruslan in loser_l:
    print('Тимур')
elif Timur == 'Спок' and Ruslan in loser_sp:
    print('Тимур')
else:
    print('Руслан')

# better solution

# Timur = input()
# Ruslan = input()
# l_1 = ['камень', 'бумага', 'ножницы', 'камень', 'ящерица', 'Спок', 'ножницы', 'ящерица', 'бумага', 'Спок']
# l_2 = ['ножницы', 'камень', 'бумага', 'ящерица', 'Спок', 'ножницы', 'ящерица', 'бумага', 'Спок', 'камень']
# if Timur == Ruslan:
#     print('ничья')
# elif l_1.index(Timur) == l_2.index(Ruslan):
#     print('Тимур')
# else:
#     print('Руслан')



