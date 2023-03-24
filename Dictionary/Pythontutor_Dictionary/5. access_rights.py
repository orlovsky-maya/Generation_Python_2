actions_dict = {'read': 'R', 'write': 'W', 'execute': 'X'}
n = int(input())
my_dict = {i[0]: i[1:]for i in [input().split() for _ in range(n)]}
m = int(input())
for j in range(m):
    action, name_file = input().split()
    action = actions_dict[action]
    if action in my_dict[name_file]:
        print('OK')
    else:
        print('Access denied')

#  reference solution
ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')
