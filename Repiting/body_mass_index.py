massa = float(input())
height = float(input())
body_mass_index = massa / height ** 2
if body_mass_index < 18.5:
    print('Недостаточная масса')
elif 18.5 <= body_mass_index <= 25:
    print('Оптимальная масса')
else:
    print('Избыточная масса')
