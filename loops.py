# easy:
# problem-1:
#  Print all numbers from 1 to 100 using a  for  loop. 
# for i in range(1,101):
#     print(i)

# # problem-2:
# # # Write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2) 
# # # way-1
# # n = int(input("Enter the value of n: "))
# # sum=0
# # for i in range(1,n+1):
# #     sum+=i
# # print(f"sum of first {n} natural numbers is {sum}")

# # # way-2:
# # n = int(input("Enter the value of n: "))
# # sum = n*(n+1)//2
# # print(sum)

# # problem-03:
# # all even numbers between 1 and 50 using a  while loop
# num=1
# while(num<51):
#     if num%2==0:
#         print(num)
#     num+=1 

# # problem-04:
# # a program to display the multiplication table of a given number. First 20

# number = int(input("enter the number: "))
# for i in range(1,21):
#     print(f"{number} x {i} = {number*i}")

# # problem-05:
# # reverse a number using a  while  loop. 
# # 1.  Also can we get the sum of all the digits.

# number = int(input("Enter the number: "))
# temp = number
# sum = 0
# rev = 0
# while(number>0):
#     last = number % 10
#     sum+=last
#     rev=rev*10+last
#     number//=10
# print(f"reverse of {temp} is {rev}")
# print(f"sum of digits of {temp} is {sum}")

# program to count the number of digits in a given number using a  while  loop. 

input = 12345
count = 0
while(input>0):
    input//=10
    count+=1
print(count)

# program that keeps asking the user to enter numbers until they enter a negative number. Use a  while  loop. 

num1 = int(input("enter a number: "))
while(num1>0):
    num1 = int(input("enter the number: "))
print(num1)

 
# Print the first 10 terms of the Fibonacci series using a  for loop.
 
   















# Check if a given number is a prime number using a  for loop. 
num = int(input("Enter a number: "))
if(num==1):
    print("1 is neither prime nor composite")
else:
    isprime = True
    for i in range(2,num):
        if num%i==0:
            isprime=False
            break
    if isprime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

# Write a program to calculate the factorial of a number using a  while  loop. 




# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop. 
# Implement a menu-driven program where the user can 
# choose to: 
# 1.  Find the square of a number. 
# 2.  Find the cube of a number. 
# 3.  Exit. 
# Implement a basic login system where the user has three attempts to enter the correct password using a loop.
