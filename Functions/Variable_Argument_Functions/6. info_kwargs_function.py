def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(key + ':', value)


# # input
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
# # output
# age: 28
# first_name: Timur
# job: teacher
# last_name: Guev