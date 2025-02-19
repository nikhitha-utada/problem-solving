# # write a program to check if a given number is +ve,-ve or zero
# num = int(input("Enter the number: "))  # for more better output take input as float
# if(num==0):
#     print("It is zero")
# elif(num>0):
#     print("It is a positive number")
# elif(num<0):
#     print("It is a negative number")
# else:
#     print("Enter valid input")

# # Determine if a number is even or odd
# num = int(input("Enter the number: "))
# if(num%2==0):
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# # ternary operator:
# # var_name = answer if condition else statement 
# result = "Even" if num%2==0 else "Odd"

# # Check if a person is eligible to vote
# age = int(input("Enter the age of the person: "))
# if(age >= 18):
#     print("Congratulations!!! You are eligible to vote")
# else:
#     print("Sorry you are not eligible to vote")
# # ternary operator:
# is_eligible = "Eligible" if age>=18 else "Not eligible"

# # Write a program to find the greatest of 2 numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if(num1>num2):
#     print(f"{num1} is greatest among {num1} and {num2}")
# elif(num2>num1):
#     print(f"{num2} is greatest among {num1} and {num2}")
# else:
#     print("Both are equal")

# # print "pass" if a student scores more than 40 marks otherwise print "fail"
# marks = int(input("Enter the marks you scored: "))
# if(marks>40):
#     print("Pass")
# else:
#     print("Fail")

# # ternary operator:
# passed = "Pass" if marks>40 else "Fail"

# # write a program to display the day of the week based on the number input (1 for monday, 2 for tuesday,....)

day = input("Enter the day of the week: ")
match day:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5": 
        print("Friday")
    case "6":
        print("Saturday")
    case "7":
        print("Sunday")
    case _:
        print("Enter valid input")

