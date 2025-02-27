# easy:
# problem-1:
#  Print all numbers from 1 to 100 using a  for  loop. 
for i in range(1,101):
    print(i)

# problem-2:
# Write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2) 
# way-1
n = int(input("Enter the value of n: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"sum of first {n} natural numbers is {sum}")

# way-2:
n = int(input("Enter the value of n: "))
sum = n*(n+1)//2
print(sum)