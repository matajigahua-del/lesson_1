# Topics to be covered today:
# 1. Methods: A method is a function that lives inside a class and work's upon an object's data. Think of it as a function that belongs to an object. Every method automatically receives self as the first parameter.

# Example for method: 
# class Student:
#     def greet(self,name):
#         self.name=name
#         print(f"Hello , I'm a student, my name is: {name} ")
# s=Student()
# s.greet("Alpha")

# 2. Constructor: A constructor is a special method that runs automatically the moment you create an object. In python its called __init__. Its job is to set up the initial state (attributes) of the object.

# Example: 
# class Student:
#     def __init__(self,name,age):
#         self.name=name #attribute
#         self.age=age

#     def show(self):
#         print(f"{self.name} is {self.age} old")

# s1=Student("Riya",20)
# s1.show()

# 3. Destructor: A destructor is the opposite, it runs automatically when  an object is about to be destroyed (garbage colled). In python its _del__:

# Example:
# class Student:
#     def __init__(self,name):
#         self.name=name #attribute
#         print(f"{self.name} created.")

#     def __del__(self):
#         print(f"{self.name} destroyed.")

# s1=Student("Riya")
# del s1


# 4. enumerate: It helps you loop over with an index.
# Example:
# noramlly loop over:
# fruits=["apple","mango","kiwi","guava"]

# i=0
# for fruit in fruits:
#     print(i,fruit)
#     i+=1

# enumerate()

# for i,fruit in enumerate(fruits,start=1):
#     print(i,fruit)

# obj1=enumerate(fruits)
# print(list(obj1)[1])

# 5. Major concepts of OOPs: 
# 1.Inheritance 
# 2.Encapsulation 
# 3.Polymorphism
# 4.Abstraction

cars=["Range Rover","Ferrari","Bugatti","lamborghini"]
# i=0
# for car in cars:
#     print(i,car)
#     i+=1



for i,car in enumerate(cars,start=2):
    print(i,car)
obj1=enumerate(cars)
print(list(obj1)[3])
