def greet(name, *args):
    if len(args) == 0:
        return f'Hello, {name}!'
    else:
        return f'Hello, {name} and {" and ".join(args)}!'

# # input
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))
# # output
# Hello, Timur!
# Hello, Timur and Roman!
# Hello, Timur and Roman and Ruslan!

#  reference solution
def greet(name, *args):
    return f'Hello, {" and ".join((name,) + args)}!'

