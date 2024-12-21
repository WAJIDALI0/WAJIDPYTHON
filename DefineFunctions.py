# HOW TO WE CAN DEFINE FUNCTIONS IN PYTHONS
def functionname():
    print(" when we define a function then we def keyword used and and function name : ")
    print(" THIS is declare simple pattern function :")


functionname()


#  parameter pass functions
def parameter(a, b):
    print(a + b)


parameter(3, 6)


#  return function
def returns(a=5, b=4):
    c = a * b
    return c


print(returns(7, 5))


# how to we can declare class
class First:
    print("when we define a class we used class keyword")


# how to we can declare functions inside the class
class Function:
    A = 10
    print(A)

    def ClassFuntion(self, name="python coding "):
        # when we can use any variable that is defined in class and we want to used
        #  variable inside the calss function then we call as self.variablename
        print(self.A)
        print('when we can define a function inside the class then a build in parameter as self ')
        print(name)
        # we define  variables inside the clss function as
        self.B = 5
        self.c = self.A * self.B  # it gives as an error because we not used as self.a and         print(c)
        print(self.c)


#         we can define variables inside the class function without (self) keyword
obj = Function()
obj.ClassFuntion()
