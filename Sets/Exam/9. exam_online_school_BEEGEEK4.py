leader = {i for i in input().split()}
assistant = {i for i in input().split()}
print(*sorted(leader | assistant))