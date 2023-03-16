def read_csv():
    with open('data.csv') as table:
        result = []
        keys = table.readline().rstrip().split(',')
        for line in table:
            value = line.strip().split(',')
            result.append(dict(zip(keys, value)))
        return result

print(read_csv())

def read_csv():
    with open('data.csv') as file:
        keys = file.readline().strip().split(',')
        return [dict(zip(keys, line.strip().split(','))) for line in file]