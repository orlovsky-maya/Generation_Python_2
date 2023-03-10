password = input()

conditions = [lambda x: x.isdigit(), lambda x: x.islower(), lambda x: x.isupper()]


def check_password(password, conditions):
    if len(password) < 7:
        return False
    else:
        for cond in conditions:
            if any(map(cond, password)) == 0:
                return False
        return True


if check_password(password, conditions):
    print('YES')
else:
    print('NO')


import string as s

pswd = input()
is_upper_in_pswd = any(map(lambda x: x in pswd, s.ascii_uppercase))
is_lower_in_pswd = any(map(lambda x: x in pswd, s.ascii_lowercase))
is_digit_in_pswd = any(map(lambda x: x in pswd, s.digits))
print(['NO', 'YES'][all([len(pswd) > 6, is_digit_in_pswd, is_lower_in_pswd, is_upper_in_pswd])])

# s = input()
# print('YES' if all((any(i.isupper() for i in s),
#                     any(i.islower() for i in s),
#                     any(i.isdigit() for i in s),
#                     len(s) >= 7)) else 'NO')