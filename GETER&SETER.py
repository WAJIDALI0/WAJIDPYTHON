class A:
    aa=77
    def function(self):
        print('hi wajid this is oop ')
    def __init__(self):
        self.c=self.aa-40
        print('this is constructor',self.c)
    def f1(self,a):
        print('this is argument  pass function',a)
    def f2(self):
        self.bb=self.aa-7
        print('this is way ',self.bb)

        print('this get value of variable that is declared in  calss ,',self.aa)
    #  THIS IS GETTER AND SETTER FUNCTION
    def getter(self,val):
        self.name=val
    def setter(self):
        return self.name

    # this is  inheritance

class Parent:
    def single(self):
        print('this is  parent class')
# single inheritance
class Child():

    def child(self):
        print(' this is child class it is single inheritance')
 # class Child(Parent):
 #
 #    def child(self):
 #        print(' this is child class it is single inheritance')
#    multilevel inheritance
# class Multilevel(Child):
#     def mul(self):
#        print('this is multilevel inheritance')
#             Multiple inheritance
class Multiple(Parent , Child):
    def multiple(self):
        print('this is multiple inheritance ')


#  how to we can create object of any class ..
#  according to this way

obj=A()
obj.function()
obj.f1(23)
obj.f2()
obj.getter(66)
store=obj.setter()
print(store)
#
obj1=Parent()
obj1.single()
#
obj2=Child()
obj2.child()
# obj2.single()
#
# obj3=Multilevel()
# obj3.single()
# obj3.child()
# obj3.mul()
#
obj4=Multiple()
obj4.multiple()
obj4.child()
obj4.single()
