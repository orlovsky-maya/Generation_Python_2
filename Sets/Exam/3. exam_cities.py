n = int(input())
cities = {input() for _ in range(n)}
next_city = input()
if next_city in cities:
    print('REPEAT')
else:
    print('OK')
    cities.add(next_city)