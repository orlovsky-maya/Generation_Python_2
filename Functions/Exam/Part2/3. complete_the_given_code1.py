words = 'the world is mine take a look what you have started'.split()
print(*list(map(lambda x: '"' + x + '"', words)))


