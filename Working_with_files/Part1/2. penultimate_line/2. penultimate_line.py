name = input()
file = open(name)
text = file.readlines()[-2]
print(text)
file.close()