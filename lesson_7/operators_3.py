# Python Operators 3

# Identity Operators: If two variables are the same object in memory, they are identical. The 'is' operator returns True if both variables point to the same object, while 'is not' returns True if they do not.
# Example:

# a =[1,2,3,4,5]   # Create a list.
# b=[1,2,3,4,5]    # Create another list with the same values.
# c = a            # c is pointing to the same list as a.

# print (a is c)       # True
# print (a is b)       #False
 
# print (a is not c)   #False
# print (a is not b)   #True

# Membership Operators: Its like a detective, it helps us search for anything inside a collection, i.e. lists, strings, tuples and other sequences. The 'in' operator returns True if a value is found in the specified sequence, while 'not in' returns True if it is not found. 
# Example:

a =[1,2,3,4,5]   # Create a list.
b=[1,2,3,4,5]    # Create another list with the same values.
c = a            # c is pointing to the same list as a.

print (a in b)       # True
print (a not in b)   # False
 
print (a in c)       # True
print (a not in c)   # False

# Example 2:

# Checking in strings

# sentence = 'Hello World'


# print('Hello' in sentence)      # True - 'Hello' is found!

# print('Python' in sentence)     # False - 'Python' not found

# print('xyz' not in sentence)    # True - 'xyz' is NOT there