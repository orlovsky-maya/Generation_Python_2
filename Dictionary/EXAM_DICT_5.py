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


d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

print(sum([k for i in input() for k, v in d.items() if i in v]))

