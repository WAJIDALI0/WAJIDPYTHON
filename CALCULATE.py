print("""
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVID 
""")
num=int(input('ENTER THE  FIRST VALUE : '))
num1=int(input('ENTER THE SECOND VALUE :'))
opr=input('ENTER THE OPERATOR : ')
if opr=='+':
    print(' SUM OF TWO VALUES ARE :',num+num1)
elif opr=='-':
    print('SUBTRACTING OF TWO VALUES ARE :',num-num1)
elif opr=='*':
    print(num*num1)
elif opr=='/':
    print(num/num1)
else:
    print('INVALID OPERATOR')


