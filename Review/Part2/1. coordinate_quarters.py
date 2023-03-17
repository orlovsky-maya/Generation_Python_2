main_list = [input() for i in range(int(input()))]
first_quarter = 0
second_quarter = 0
third_quarter = 0
fourth_quarter = 0
point_list = [c.split() for c in main_list]
for j in range(len(main_list)):
    if int(point_list[j][0]) > 0 and int(point_list[j][1]) > 0:
        first_quarter += 1
    elif int(point_list[j][0]) < 0 and int(point_list[j][1]) > 0:
        second_quarter += 1
    elif int(point_list[j][0]) < 0 and int(point_list[j][1]) < 0:
        third_quarter += 1
    elif int(point_list[j][0]) > 0 and int(point_list[j][1]) < 0:
        fourth_quarter += 1

print('Первая четверть:', first_quarter)
print('Вторая четверть:', second_quarter)
print('Третья четверть:', third_quarter)
print('Четвертая четверть:', fourth_quarter)
