# l=[]
# while True:
#     c=int(input('''
#      1  Push Element
#      2 Pop Element
#      3 Peek Element
#      4 Display Element
#      5 Exit
#
#      '''))
#     if c==1:
#         n=input('Enter the value :')
#         l.append(n)
#         print(l)
#     elif c==2:
#         if len(l)==0:
#             print('list is empty')
#         else:
#             p=l.pop()
#             print(p)
#             print(l)
#
#     elif c==3:
#         if len(l)==0:
#             print('Stack is empty')
#         else:
#             print('peek function :',l[-1])
#     elif c==4:
#             print('Display value :',l)
#     elif c==5:
#             break
#     else:
#         print('Invalid list')
#

l=[]
while True:
    c = int(input('''
     1  Push Element
     2 del Element in Q
     3 first  Element
     4 last element
     4 Display Element
     5 Exit

     '''))
    if c == 1:
        n = input('Enter the value :')
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print('list is empty')
        else:
            del l[0]
            # print(p)
            print('delete element is  QAueu',l)
    elif c==3:
        if len(l)==0:
            print('Epmty Q hai')
        else:
            print('First element in q :',l[0])
    elif c == 4:
        if len(l) == 0:
            print('Queue  is empty')
        else:
            print('last value in queue :', l[-1])
    elif c == 5:
        print('Display value :', l)
    elif c == 6:
        break
    else:
        print('Invalid list')

