#Assignment Operators: They are used to assign values to variables. The most common assignment operator is the equal sign (=), with new values, often combining arthematic or bitwise operations.
# = is the basic assignment operator, which assigns the value on the right to the variable on the left.
# += is the addition assignment operator, which adds the value on the right to the variable on the left and assigns the result back to the variable on the left.
# -= is the subtraction assignment operator, which subtracts the value on the right from the variable on the left and assigns the result back to the variable on the left.
# *= is the multiplication assignment operator, which multiplies the variable on the left by the value on the right and assigns the result back to the variable on the left.
# /= is the division assignment operator, which divides the variable on the left by the value on the right and assigns the result back to the variable on the left.
# %= is the modulus assignment operator, which takes the modulus of the variable on the left by the value on the right and assigns the result back to the variable on the left.
# **= is the exponentiation assignment operator, which raises the variable on the left to the power of the value on the right and assigns the result back to the variable on the left.
# //= is the floor division assignment operator, which performs floor division on the variable on the left by the value on the right and assigns the result back to the variable on the left.

#Logical operators used for logical operations such as and , or & not. They are used to combine conditional statements.

#Activity :
# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
#    Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.

# 3) Print the total marks stored in `sum`.

# 4) Calculate the percentage:
#    - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
#    - Multiply the result by 100
#    Store the final value in `perc`.

# 5) Print the percentage stored in `perc`.

#Activity:
math=int(input("Enter marks for math: "))
english=int(input("Enter marks for english: "))
science=int(input("Enter marks for science: "))
hindi=int(input("Enter marks for hindi: "))
sum=math+english+science+hindi
print("Total marks:",sum)
perc=(sum/400)*100
print("percentage:",perc)
