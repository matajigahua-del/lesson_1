import array as arr

# Sets & Arrays:


# Sets : It is a collection of unique and unordered elements, even if we add an element more than once in a set, it will be considered only once. So no duplicates. In sets there is no concept of indexes.

# Operations on sets:
# creation: 
# my_set={1,2,3,3,4,4,5,5,5}
# print(my_set)

# adding an element: to add we use set.add(element)
# my_set={1,2,3,3,4,4,5,5,5}
# my_set.add(7)
# print(my_set)

# Intersection- To find data present in both sets,we use intersection function.

# Example:
# my_set1={1,2,3,4,5,6}
# my_set2={2,4,5,9,6,1}

# print("Intersection using .intersection: ",my_set2.intersection(my_set1))
# print("Intersection using &: ",my_set1 & my_set2)

# Union: Combines all the elemets from both sets(no duplicates), uses .union() or '|', 
# Difference: Elements in set A but not in set B , uses .difference() or '-' ,
# Symmetric difference: Elements in either set, but not in both (opposite of intersection) uses .symmetric_differnence() or '^'.
# Example:

# print("Union using .union(): ", my_set1.union(my_set2))
# print("Union using |: ", my_set1|my_set2)

# print("Difference using .differnce(): ", my_set1.difference(my_set2))
# print("Difference using - : ", my_set2-my_set1)

# print("Symmetric difference using .symmetric_difference(): ", my_set1.symmetric_difference(my_set2))
# print("Symmetric difference using ^ : ", my_set1^my_set2)


# Arrays: A collection of items stored in contiguous/consecutive memory space, to use array we need to import it first.Lists can be treated as an array, it can contain multiple data types, all the elements should be of same data types.

# Opertions on arrays:

# Creating an array: 'i': integer, 'f': float, 'd': double, 'u':unicode char
a=arr.array('i',[1,2,3])
b=[10,20,10,34]
c=["Yes","No","Sus"]

# insert: adding an element to the array we can add it to any particular position, if an element is already present at an index and inside insert we use that index then the pre-existing elements index is moved by 1.
# append: adding an element to array's end.

# Example: 

print(a.insert(2,25))
print(a,"Line 57")

print(a.append(89))
print(a,"Line 60")





# print(a,b,c)


