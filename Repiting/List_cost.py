s = input()
cost_rubl = len(s) * 60 // 100
cost_cop = len(s) * 60 % 100
print(cost_rubl, 'р.', cost_cop, 'коп.')

