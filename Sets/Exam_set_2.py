indi = [int(i) for i in input().split()]
indi_set = set(indi)
print(len(indi) - len(indi_set))