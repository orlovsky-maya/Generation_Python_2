
n = int(input())
mylist = [input() for word in range(n)]



def summa_values(word):
    word = list(word.upper())
    numbers = sum(list(map(lambda x: ord(x) - ord('A'), word)))
    return numbers

result = sorted(sorted(mylist), key=lambda x: summa_values(x))
print(*result, sep='\n')
