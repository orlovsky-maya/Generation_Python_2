data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
        'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

alf_sorted = sorted(data)
len_sorted = sorted(alf_sorted, key=lambda word: len(word))

print(*len_sorted)

#  reference solution
print(*sorted(data, key=lambda x: (len(x), x)))
