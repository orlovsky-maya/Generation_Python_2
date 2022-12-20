# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# last = countries[-1]
# print(last)

# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
# print(primes[:6])



# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[2:])

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[:-3])

# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:-2])


#
# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
# number = len(countries)
# print(number)

# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
# summa = max(numbers) + min(numbers)
# print(summa)

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)

# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
# number = countries.count('Spain')
# print(number)


# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

#
# city_name = input()
# city_year = int(input())
# city = (city_name, city_year)
# print(city)


# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [tuples[i] for i in range(len(tuples)) if len(tuples[i]) != 0]
# print(non_empty_tuples)
#
# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = []
# for i in range(len(tuples)):
#     if tuples[i] != ():
#         non_empty_tuples.append(tuples[i])
# print(non_empty_tuples)
#
#
# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [i for i in tuples if i]
#
# print(non_empty_tuples)


tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = []
for i in range(len(tuples)):
    elem = list(tuples[i])
    elem[-1] = 100
    tuples[i] = tuple(elem)
    new_tuples.append(tuples[i])
print(new_tuples)



tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1] + (100,) for i in tuples]
print(new_tuples)