def build_query_string(params):
    mylist = []
    for key, value in sorted(params.items()):
        mylist.append(key + '=' + str(value))
    mylist = '&'.join(mylist)
    return mylist

# mydict = {'sport': 'hockey', 'game': 2, 'time': 17}
# print(build_query_string(mydict))


def build_query_string(params):
    res = [f'{k}={v}' for k, v in params.items()]
    return '&'.join(sorted(res))