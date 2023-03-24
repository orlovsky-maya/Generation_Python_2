with open(input()) as file:
    result = []
    file = file.readlines()
    for i in range(len(file)):
        if file[i].startswith('def ') and not file[i - 1].startswith('#'):
            result.append(file[i])
    if len(result) == 0:
        print('Best Programming Team')
    else:
        for name in result:
            ind = name.find('(')
            print(name[4:ind])
