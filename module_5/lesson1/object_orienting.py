# What is Object-Oriented Programming(OOP): OOP is a way of writing code that models real-world things. Instead of functions and variables, we group related data and behaviour together into "objects".
# Real-world Example: Think of a car, a car har 
# -Properties(color, brand, speed)
# -Behaviors(start, stop, accelerate)

# OOP's lets us represent this in code the same way- bundling data (properties ) and functions(behaviors) into one unit.

# Class: A clss is template or a blueprint. It do not do anything by itself, it just defines what something looks like once its created.

# Example for class:

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# Object: An object is an actual thing created from the class.
# Example:
# my_car=Car()
# your_car=Car()
# Here, my_car & your_car are two seperate objects, both created using the same Car class. This process is called instantiation (creating an instance)

# Attributes and Their types:
# Attributes: Attributes are data that belongs to an object(like color, brand, speed).

# Two type of Attributes:

# a) Instance attributes- unique to each object.
# Example for Instance attribute: 
# class Car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
# car1=Car("Toyota","Red") #"Tyota" & "Red" are called attributes.
# car2=Car("Honda","Blue") # car1=Car("Range Rover","Black")

# # b) Class attributes- shared by all obejcts of that class.
# # Example for Class Attributes:
# class Car:
#     wheels=4 #class attribute # Class car:
#     #Breaks=1

#     def __init__(self,brand):
#         self.brand=brand # instance attribute

# car1=Car("BMW")

# print(car1, "This is class attributes example")


# # __init__ method: It's a special method that runs automatically the moment you create an object. Its used to set-up(initialize) the object's starting data.

# # self Keyword: It represents the specific object calling the method.

# # Example without OOP:
# # student_1="Amit"    book_1="Harry Potter"
# # student_1_marks=85   book_1_pages=456


# # student_2="Priya"   book_2="Lord of Kings"
# # student_2_marks=92   book_2_pages=654

# # def show_result(name,marks): def show_result(book_name,pages)
# #     print(f"{name} scored {marks}")   print(f"{book}has{pages}pages")

# show_result(student_1,student_1_marks)  show result(book_1,pages_1)
# show_result(student_2,student_2_marks)  show result(book_2,pages_2)


# # Example with OOP:

# class Student:

#     def __init__(self,name,marks,subject,grade):
#         self.name=name
#         self.marks=marks 
#         self.subject=subject
#         self.grade=grade
  

#     def show_result(self):
#       print(f"{self.name} scored {self.marks}")

# students=[Student("Amit",85,"Maths",6), Student("Priya",92,"English",8), Student("Kashvee",89,"Maths",9)]

# for i in students:
#     i.show_result()


class books:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages 
    def show_book(self):
        print(f"{self.title} has {self.pages} pages")
books_list=[books("Harry Potter",456),books("Lord of Kings",678)]
for i in books_list :
          i.show_book()