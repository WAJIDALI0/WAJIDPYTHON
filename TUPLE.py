from itertools import count

t=(3,5,45,6)
print(t)
for va in t:
    print(va)
l= len(t)
for v in range(l):
    print(t[v])

    # some funtions of tuples

tt=(4,4,34,33,45)
c=tt.count(4)
print('this is count funtion ',c)
mx=max(tt)
print('this is maximum function ',mx)
mn=min(tt)
print('this is min function',mn)
s=sum(tt,12)
print('this is sum funtion and it sum all values in (tt) and add 12 in sum of tuple',s)
i=tt.index(45)
print('this is index function ',i)
# count ,sum ,min, max ,index   syntax: ()