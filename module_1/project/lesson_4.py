start=int(input("enter the starting number - "))
end=int(input("enter the ending number - "))
squares=[i**2 for i in range(start,end+1)]
even_squares=[i for i in squares if i%2==0]
odd_squares=[i for i in squares if i%2!=0]
print(f"Squares of numbers from {start} to {end} are {squares}")
print(f"Even squares of numbers from {start} to {end} are {even_squares}")
print(f"Odd squares of numbers from {start} to {end} are {odd_squares}")