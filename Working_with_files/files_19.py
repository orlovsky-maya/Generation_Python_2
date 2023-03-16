with open('class_scores.txt', 'r') as old_scores, open('new_scores.txt', 'w') as new_scores:
    for line in old_scores:
        name, score = line.split()
        new_scores.writelines(f'{name} {int(score) + 5}''\n')