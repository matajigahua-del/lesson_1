# Tuples: Immutable, heterogeneous data are unchangeable, it means that it can store various data types or variables of all types.
# Creating a Tuple: using() or using tuple(), the items will be seperated with commas.
# Example: 

# Str="String"
# Operations: Indexing, Slicing, Changing a Tuple, Concatenation of a Tuple,  Nested Tuple.
# Indexing : To acess a element using its position or index.
# Example:

# li=[1,25,17,258,45] #starting:0, ending:length

# for i in li:  #i=0: 1 , i=1: 25 .... 45
#     print(i)

# Example for indexing: 
# number_tuple=(5,7,8,95,140)
# print("Element at index 3: ",number_tuple[3])

# for i in range(5):
#     print(number_tuple[i])

# Example for slicing: 
# tuple1=('P','Y','T','H','O','N')

# print(tuple1[3:6])

#Changing a Tuple: Tuples are immutable, it means that element of the tuple cannot be changed once they have been assigned. But , if element is itself a mutuable data type as a list, its nested items can be changed.

#Example of changing:

# tuple1= (1,2,3,54,[1,5,7,8],75)
# tuple1[4][2]=95

# print(tuple1[4])

# Example of Concatenation:

# tuple1=('P','Y','T','H','O','N')
# tuple2=(1,5,9)

# print(tuple1+tuple2)

# Example Of nested Tuples: 

# nested_tup=(1,2,(8,9),4,5,[1,5,'nesting'])

# print(nested_tup)
# print(nested_tup[2]) #(8,9)
# print(nested_tup[-1][-1]) # nesting



# DICTIONARY: They are unordered and mutable collection of data values used to store data values in key-value pairs. They are stored in curly brackets, we use colon to seperate key from value and commas to seperate different pairs.To access elements we use keys.

# Methods used in dictionary: len(dict), dict.clear():Removes all elements, dict.copy(): Return a shallow copy of dictionary, dict.items(): returns a new object of the dictionary's items in key-value format, dict.popitems(): Removes and returns an item(key-value), if dictionary is empty throws an keyError, dict.values(): Return new object with the dictionary's values, dict.get(key[,d]): Returns the value of key, if the key is not present it returns default.

# Example of accessing elements through Keys:

# my_dict={'Name':'Alex', 'Age':7,'Class':'First'}
# print(my_dict['Name']) #output : Alex

# Exmaple of add new items and updating values:
# my_dict={'Name':'Alex', 'Age':7,'Class':'First'}

# #updating
# my_dict["Age"]=67 
# print("Updated the age to 67",my_dict)

# # add new item:
# my_dict['Gender']='Male'

# print("Added Gender to the dictionary", my_dict)

# delete an element or item: It means that we want to remove a particular element from the dictionary by using dict_name.pop(key).

# square={1:1,2:4,3:9,4:16,5:25}

# # Remove a particular item and return its value:
# print("Removed item with key 4: ",square.pop(4)) #o/p: 4:16

# print("Showing the updated dictionary ",square) # No 4:16 will not be present.

# # Remove an arbitary (last inserted) item, return (key,value)
# square[6]=36
# print("Using the popitem to remove any item: ",square.popitem()) #5:25

# print("Printing the updated dictionary: ",square)

# Iterate through a dictionary:
square={1:1,2:4,3:9,4:16,5:25}
for i in square:
    print(square[i])


# tuple1=(1,5,6,7,[8])
# tuple1[4][-1]=95
# print(tuple1[4])
# # print(dic_1)

# dic_1={"Name":"Lex","Age":7,"Gender":"male"}
# dic_1["Gender"]="female"
# dic_1["English marks"]=67
# print(dic_1)


