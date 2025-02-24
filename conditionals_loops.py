# question-1:   
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

# question-2:
# Determine if a number is even or odd
num = int(input("Enter the number: "))
if(num%2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# ternary operator:
# var_name = answer if condition else statement 
result = "Even" if num%2==0 else "Odd"

# question-3:
# Check if a person is eligible to vote
age = int(input("Enter the age of the person: "))
if(age >= 18):
    print("Congratulations!!! You are eligible to vote")
else:
    print("Sorry you are not eligible to vote")
# ternary operator:
is_eligible = "Eligible" if age>=18 else "Not eligible"

# question-4:
# Write a program to find the greatest of 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if(num1>num2):
    print(f"{num1} is greatest among {num1} and {num2}")
elif(num2>num1):
    print(f"{num2} is greatest among {num1} and {num2}")
else:
    print("Both are equal")

# question-5:
# print "pass" if a student scores more than 40 marks otherwise print "fail"
marks = int(input("Enter the marks you scored: "))
if(marks>40):
    print("Pass")
else:
    print("Fail")

# ternary operator:
passed = "Pass" if marks>40 else "Fail"

# question-6:
# write a program to display the day of the week based on the number input (1 for monday, 2 for tuesday,....)

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

# question-7:
# calculator
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
        
    if operator == '+':
            result = num1 + num2
    elif operator == '-':
            result = num1 - num2
    elif operator == '*':
            result = num1 * num2
    elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
    else:
            print("Invalid operator! Please use +, -, *, or /.")
            return
        
print(f"Result: {result}")
calculator()

#Question8
# Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).
num = int(input("Enter a number: "))

if num == 1:
    print("January")
elif num == 2:
    print("February")
elif num == 3:
    print("March")
elif num == 4:
    print("April")
elif num == 5:
    print("May")
elif num == 6:
    print("June")
elif num == 7:
    print("July")
elif num == 8:
    print("August")
elif num == 9:
    print("September")
elif num == 10:
    print("October")
elif num == 11:
    print("November")
elif num == 12:
    print("December")
else:
    print("Invalid input! Enter a number between 1 and 12.")

# Medium Questions

#  Question-1
# program to find the greatest of three numbers.
def greatestNumber(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        return num3
    elif num2>num3:
        return num2
    return num3
print(greatestNumber(10,20,30))

#  Question-2
# Check if a year is a leap year. 
year = int(input("Enter the year: "))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("not a leap year")

# Question-3:
# Write a program to classify a character entered by the user as a vowel, consonant, or neither.

ch = input("Enter the character: ")
if(ch.isalpha()):
    if(ch in ["a","e","i","o","u"]):
        print("Its a vowel")
    else:
        print("Its a consonant")
elif(ch.isdigit()):
    print("Its a digit")
else:
    print("INVALID CHARACTER")

# QUESTION-4:
# Calculate the grade of a student based on the marks they score: 
# 1.  90-100  : Grade A 
# 2.  80-89  : Grade B 
# 3.  70-79  : Grade C 
# 4.  <70  : Fail. 

marks = int(input("Enter the marks: "))
if(marks>=90 and marks<=100):
    print("Grade is A")
elif(marks>=80 and marks<=89):
    print("Grade is B")
elif(marks>=70 and marks<=79):
    print("Grade is C")
else:
    print("Fail")

# Question-5:
# Write a program to check if three sides length form a valid triangle.
s1 = int(input("Enter side1: "))
s2 = int(input("Enter side2: "))
s3 = int(input("Enter side3: "))
if((s1+s2)>s3 and (s2+s3)>s1 and (s3+s1)>s2):
    print("valid triangle")
else:
    print("invalid triangle")
