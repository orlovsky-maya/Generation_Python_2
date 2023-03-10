n = int(input())
ip_list = [input().split('.') for i in range(n)]


def convert_10(ip_adress):
    mylist = []
    for i in range(len(ip_adress)):
        mylist.append(int(ip_adress[i]) * 256 ** (len(ip_adress) - (i + 1)))
    return sum(mylist)


sorted_list = sorted(ip_list, key=convert_10)

for l in sorted_list:
    print('.'.join(l))
