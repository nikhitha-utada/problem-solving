# write a program to check if a given number is +ve,-ve or zero
num = int(input("Enter the number: "))  # for more better output take input as float
if(num==0):
    print("It is zero")
elif(num>0):
    print("It is a positive number")
elif(num<0):
    print("It is a negative number")
else:
    print("Enter valid input")

# Determine if a number is even or odd
num = int(input("Enter the number: "))
if(num%2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Check if a person is eligible to vote
age = int(input("Enter the age of the person: "))
if(age >= 18):
    print("Congratulations!!! You are eligible to vote")
else:
    print("Sorry you are not eligible to vote")

# Write a program to find the greatest of 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if(num1>num2 or num1==num2):
    print(f"{num1} is greatest among {num1} and {num2}")
else:
    print(f"{num2} is greatest among {num1} and {num2}")



