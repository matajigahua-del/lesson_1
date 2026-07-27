# Topics for today:
# Inheritance
# Child class
# Parent features using __init__
# super() keyword
# Override a method
# Issubclass()

# What is inheritance? 
# In python, Inheritance is when one class(child or subclass) borrows properties and behaviors from another class(parent or superclass) without having to rewrite the code. 

# Example:

# class Animal: # Its a Parent clss
#     def eat(self):
#         print("I am eating")

# class Dog(Animal): # Dog inherits from Animal so its a child
#     # def bark(self):
#     #     print("Woof!")


# d=Dog()
# d.eat() # Works, Inherited from Animal
# d.bark() # Works!, It is its own method.

# Getting Parents features with __init__(): Let's say if a child class doesn't define its own __init__, it automatically uses the parent's.

# Example:

# class Parent:
#     def __init__(self,name):
#         self.name=name

# class Child(Parent):
#     pass

# c=Child("Alex")
# print(c.name) #Alex

# super() keyword: Its how a child calls code from its parent. Mostly the parent's __init__() so we do not have to rewrite it.

# Example:

# class Parent:
#     def __init__(self,name): class Child(Parent)
#         self.name=name
#         print(f"Parent init: name set to {name}")
# class Child(Parent):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age
#         print(f"Child init: age set to {age}")

# c=Child("Alex", 10)
# print(c.name,c.age)

# Overriding a method: 

# Example:

class Animal:
    def sound(self):
        print("Some animal sound")

    def __init__(self,legs):
        self.legs=legs

class Dog(Animal):
    def sound(self): # overriding a parent method
        print("Woof!")
    def __init__(self,legs):
        super().__init__(legs)
        print(legs,"legs")  

a=Animal("Four")
a.sound() # some animal sound
print(a.legs)

b=Dog("Four")
b.sound()



