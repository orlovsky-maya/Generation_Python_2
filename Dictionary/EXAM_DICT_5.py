mydict = {('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'): 1,
          ('D', 'G'): 2,
          ('B', 'C', 'M', 'P'): 3,
          ('F', 'H', 'V', 'W', 'Y'): 4,
          ('K',): 5,
          ('J', 'X'):8,
          ('Q', 'Z'): 10}
word = input()
counter = 0
for c in word:
    for key in mydict:
        if c in key:
            counter += mydict[key]
            break
print(counter)

