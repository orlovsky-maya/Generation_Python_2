with open('grades.txt') as file:
    data = file.readlines()
    data_list = [line.strip().split() for line in data]
    counter_students = 0
    for line in data_list:
        counter_tests = 0
        for i in range(1, len(line)):
            if int(line[i]) >= 65:
                counter_tests += 1
            if counter_tests == 3:
                counter_students += 1
    print(counter_students)

#  reference solution
with open('grades.txt') as f:
    print(sum(1 for i in f.readlines() if all([int(j) >= 65 for j in i.split(' ')[1:]])))