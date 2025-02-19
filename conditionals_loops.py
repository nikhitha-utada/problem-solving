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
num = int(input("Enter the number"))
if(num%2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")