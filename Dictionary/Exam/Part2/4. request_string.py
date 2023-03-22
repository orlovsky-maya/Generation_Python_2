def build_query_string(params):
    mylist = []
    for key, value in sorted(params.items()):
        mylist.append(key + '=' + str(value))
    mylist = '&'.join(mylist)
    return mylist

#  reference solution
def build_query_string(params):
    res = [f'{k}={v}' for k, v in params.items()]
    return '&'.join(sorted(res))


# input
print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
# output
# age=28&name=timur
# game=2&sport=hockey&time=17