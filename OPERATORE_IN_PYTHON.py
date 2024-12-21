# LOGICAL OPERATORS
# and,or,not
a = 6
y = 99
print(a == 6 and y == 99)
print(a == 6 or y <= 7)
print(not a != y)  # 6!=99 its answer is true but wit (not ) change the result
#  Membership operators
#  IN and not in
s = 'my name is wajid'
print('my' in s)
print('wajid' not in s)
# identity operatores
print(a is y)
print(a is not y)
#  Bitwise Operatores
b = 3
c = 2
print(b & c)
print(bin(b & a))  # boths are true
print(b | c, bin(b | c))  # if one is true
print(b ^ c, bin(b ^ c))  # in boths conditions only one is true  if boths are true then false
