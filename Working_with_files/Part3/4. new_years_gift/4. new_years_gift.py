with open('class_scores.txt', 'r') as old_scores, open('new_scores.txt', 'w') as new_scores:
    for line in old_scores:
        name, score = line.split()
        if int(score) < 95:
            new_scores.writelines(f'{name} {int(score) + 5}''\n')
        else:
            new_scores.writelines(f'{name} {100}''\n')

#  reference solution
with open('class_scores.txt') as class_scores, open('new_scores.txt', 'w') as new_scores:
    for line in class_scores:
        name, score = line.split()
        score = int(score) + 5
        if score > 100:
            score = 100
        print(name, score, file=new_scores)