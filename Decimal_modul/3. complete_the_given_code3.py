from decimal import *
num = Decimal(input())

num_tuple = num.as_tuple()
digits = num_tuple.digits
exp = num_tuple.exponent

if len(digits) > abs(exp):
    print(min(digits) + max(digits))
else:
    print(max(digits))

#  reference solution
from decimal import *
num = Decimal(input())
cyphers = num.as_tuple().digits
print(max(cyphers) + min(cyphers) * (abs(num) >= 1))