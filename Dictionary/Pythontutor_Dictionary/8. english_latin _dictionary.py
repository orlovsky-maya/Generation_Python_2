n = int(input())
en_dict = {}
for i in range(n):
    english, *latin = input().replace('-', '').replace(',', '').split()
    en_dict[english] = latin
lat_dict = {}
for key, value in en_dict.items():
    for v in value:
        if v not in lat_dict:
            lat_dict[v] = [key]
        else:
            lat_dict[v].append(key)
print(len(lat_dict))
for key, value in sorted(lat_dict.items()):
    print(key, '-', (', ').join(value))
