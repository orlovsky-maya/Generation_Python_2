def greet(name, *args):
    if len(args) == 0:
        return f'Hello, {name}!'
    else:
        return f'Hello, {name} and {" and ".join(args)}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))




def greet(name, *args):
    return f'Hello, {" and ".join((name,) + args)}!'

