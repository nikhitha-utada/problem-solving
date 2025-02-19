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
