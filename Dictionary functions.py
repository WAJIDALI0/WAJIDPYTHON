#  today we learn get(),keys(),values(),and items
from os import popen

d={
    'name':'wajid',
    'id':71685,
    'duration':'2months'
}
# show values with get fuctions
var=d.get('name')
print(var)
# second way to get values
v=d['name']
print(v)
# get keys in dictionary  through keys() function using loop
for a in d.keys():
    print(a)
#  values() funtions
for aa in d.values():
    print(aa)
 #    items() it is used for both keys and values funtions
# it used for show all data in list
for aaa in d.items():
    print(aaa)
    # it is used for my marzi
for b,c in d.items():
    print(b)
    print(c)
    # we can delete date in dictionary using del() and pop() funtions
    # pop returns values who we delete but del() not returns
dd={'n':'WAK',
    id:54,
    'w':'pythons'
}
#  delete data with del() but we can use keys for delete date in dictionary
del dd[id]
print(dd)
# delete date with pop() but we can use keys for delete data in dictionary
#  it returns delete value
s=dd.pop('n')
print(s)
print(dd)
#  another way to define dictionary with dict() functions
sn=dict(name='my name is wajid ',id=8484)
print(sn)
# update value in dictionary
n={ 'name':'ksk',
    'ids':885,
}
n.update({'ids':8888})
print(n)

# clear dictionary
n.clear()
print(n)
#  insert data in dictionary
ins={
    'book':'English'
}
ins['book2']='Math'
print(ins)