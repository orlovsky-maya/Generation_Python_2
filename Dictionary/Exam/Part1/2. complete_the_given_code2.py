emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

emails = {key: [mail + '@' + key for mail in value] for key, value in emails.items()}
emails_list = [value for value in emails.values()]
emails_list = [emails_list[i][j] for i in range(len(emails_list)) for j in range(len(emails_list[i]))]
emails_list = sorted(emails_list)

print(*emails_list, sep='\n')

#  reference solution
print(*sorted([i+'@'+k for k, v in emails.items() for i in v]), sep = '\n')