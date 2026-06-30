number=int(input("Enter the number - "))
number=abs(number)
count=0
if number==0:
    count=1
else:
    while number>0:
        count+=1
        number=number//10
        print(f"Total number of digits in the number is,{number}")