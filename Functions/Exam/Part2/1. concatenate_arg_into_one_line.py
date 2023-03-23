def concat(*args, sep=' '):
    return sep.join(map(str, args))

# # input
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
# # output
# hello python and stepik
# hello*python*and*stepik
# hello()()()python
# hello
# 1$$2$$3$$4$$5$$6$$7$$8$$9