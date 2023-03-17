Timur = input()
Ruslan = input()
if Timur == Ruslan:
    print('ничья')

elif Timur == 'камень' and Ruslan == 'ножницы' or Timur == 'бумага' and Ruslan == 'камень' or Timur == 'ножницы' and \
        Ruslan == 'бумага':
    print('Тимур')
else:
    print('Руслан')
