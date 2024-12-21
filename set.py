# set give us answer in rondom and it only unique values not count same values
# it cannot get with index
# it is unordered data type
# we cannot update
from os import remove

s={4,6,46,4,6}
for v in s:
    print(v)
# some function are  set,pop ,remove ,discard,update,clear,add
#  set function is used for convert list,tuple into set how  esy chck
# 1............set()
l=[5,66,76,44,5]
st=set(l)
print(st)
t=(5,7,5,77,55)
stt=set(t)
print(stt)
# 2............pop()
s={4,6,43}
p=s.pop()
print(p)
# 3..........remove()
# r=s.remove(43)
# print(r)
# 4........discard()
s.discard(6)
print(s)
# 5.........update()
ts={6,7,65}
ll=[5,6,54]
ts.update(ll)
print(ts)
# 6........add()
ts.add(77)
print(ts)
# 7........clear()
ts.clear()
print(ts)

