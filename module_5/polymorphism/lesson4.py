# Topics: 
# 1. Abstraction :It means hiding the complicated details and showing only the important stuff to the used. 
# Example: 

# class CoffeeMachine:
#     def heat_water(self):   # internal detail, hidden
#         print("Heating water ...")

#     def add_coffee(self):  # internal detail, hidden
#         print("Adding coffee grounds...") 
    
#     def make_coffee(self): # simple interface which is exposed or known to us.
#         self.heat_water()
#         self.add_coffee()
#         print("Here's your coffee!...")
    
# machine=CoffeeMachine()
# machine.make_coffee()  # we called one simple method.
# class ATMmachine:
#     def insert_card(self):
#         print("Inserting the card")
#     def enter_pin(self):
#         print("Entering the pin")
#     def select_withdraw(self):
#         print("Selecting withdrawl option")
#     def enter_amount(self):
#         print("Enter the withdrawl amount")
#     def take_money(self):
#          print("Taking the money out")
#     



# 2. Abstract Class : It's a blueprint class that cannot be used to create objects directly. It exists only to be inherited, and it can force child classes to implement certain methods.

# Example:

# from abc import ABC, abstractmethod

# class Shape(ABC): # ABC= Abstract Base Class
#     @abstractmethod
#     def area(self):
#         pass         # no implementation here - child must provide one.

# class Circles(Shape):           #from abc imort ABC
#                                 #abstractmethod
#     def __init__(self, radius): #class shape(ABC)
#         self.radius = radius    #@abstractmethod
#                                #def area(self):
#                             #    pass
#     def area(self):
#         return 3.14 * self.radius **2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
        
#     def area(self):
#         return self.side ** 2

# c = Circles(5)
# print(c.area())

# s=Square(5)
# print(s.area())





# # 3. Polymorphism : Poly="Many" and morph="Forms". Polymorphism means the same method name can behave differently depending on which object it calls it.


# class Animal:
#     def Sound(self):
#         print("Make a sound")

# class Cat(Animal):
#     def Sound(self):
#         print("Meow!")

# class Dog(Animal):
#     def Sound(self):
#         print("Woof")


# animals=[Dog(),Cat(),Animal()]

# for animal in animals:
#     animal.Sound()



# Activity 1:
# 1) Import `ABC` and `abstractmethod` from the `abc` module.
#    (These are used to create abstract base classes in Python.)

# 2) Create an abstract base class named `Absclass` that inherits from `ABC`.

# 3) Inside `Absclass`, define a normal method `print(self, x)`:
#    a) It takes a value `x` as input.
#    b) It prints the value passed to the method.

# 4) Define an abstract method `task(self)` using the `@abstractmethod` decorator:
#    a) This method must be implemented (overridden) in any child class.
#    b) The print statement inside shows what the base version contains.

# 5) Create a subclass named `test_class` that inherits from `Absclass`.

# 6) Implement the abstract method `task(self)` inside `test_class`:
#    a) Print "We are inside test_class task".
#    (This satisfies the abstract method requirement.)

# 7) Create an object `test_obj` of the class `test_class`.
#    (We can create this object because `task()` is implemented.)

# 8) Call `test_obj.task()` to run the overridden method in `test_class`.

# 9) Call `test_obj.print(100)` to print the value 100 using the parent class method.


# Activity 2:
# 1) Import `ABC` and `abstractmethod` from the `abc` module.
#    (These are used to create abstract base classes in Python.)

# 2) Create an abstract base class named `Absclass` that inherits from `ABC`.

# 3) Inside `Absclass`, define a normal method `print(self, x)`:
#    a) It takes a value `x` as input.
#    b) It prints the value passed to the method.

# 4) Define an abstract method `task(self)` using the `@abstractmethod` decorator:
#    a) This method must be implemented (overridden) in any child class.
#    b) The print statement inside shows what the base version contains.

# 5) Create a subclass named `test_class` that inherits from `Absclass`.

# 6) Implement the abstract method `task(self)` inside `test_class`:
#    a) Print "We are inside test_class task".
#    (This satisfies the abstract method requirement.)

# 7) Create an object `test_obj` of the class `test_class`.
#    (We can create this object because `task()` is implemented.)

# 8) Call `test_obj.task()` to run the overridden method in `test_class`.

# 9) Call `test_obj.print(100)` to print the value 100 using the parent class method.


# Activity 3:
# 1) Create a class `India` with three methods:
#    a) `capital()` to print the capital of India.
#    b) `language()` to print the main language spoken in India.
#    c) `type()` to print the type of country India is.

# 2) Create another class `USA` with the same method names:
#    a) `capital()` to print the capital of USA.
#    b) `language()` to print the primary language of USA.
#    c) `type()` to print the type of country USA is.

# 3) Create objects for both classes:
#    a) `obj_ind = India()`
#    b) `obj_usa = USA()`

# 4) Use a common interface (polymorphism) to call the same method names
#    on different objects:
#    a) Use a `for` loop to iterate through `(obj_ind, obj_usa)`.
#    b) For each object `country`, call:
#       - `country.capital()`
#       - `country.language()`
#       - `country.type()`
#    (Each object runs its own class implementation of these methods.)


#A1
# from abc import ABC,abstractmethod
# class Absclass(ABC):
#      def print(self,x):
#          print("value =",x)
#      @abstractmethod
#      def task(self):
#              pass 
# class test_class(Absclass):
#   def task(self):
#                  print("We are inside test_class")
# test_obj=test_class()
# test_obj.task()
# test_obj.print(100)

#A3
class india:
      def capital(self):
             print("Capital:New Delhi")
      def language(self):
             print("Language:Hindi")
      def type(self):
             print("Type:Democracy")
class USA:
       def capital(self):
              print("Capital:Washington D.C")
       def language(self):
              print("Language:English")
       def type(self):
              print("Type:Democracy")
obj_ind=india()
obj_usa=USA()
for country in (obj_ind,obj_usa):
 country.capital()
 country.language()
 country.type()
 print()
              
       
