# datatypes:
int_num = 5
float_num = 9.8
complex_num = 5+9j
bool_val = True
str = "Hello"
my_lst = [2,4,5]
my_tuple = (3,5,7)
my_dict = {"jhi":5,"jfs":10}
my_set={3,4,4}
print(type(int_num))
if 2>4:
    print("true")
elif 5>7:
    print("false")
else:
    print("wrong")
for i in range(my_lst):
    print(i)
for i in range(my_tuple):
    if(i==3):
        break
    print(i)
for i in range(my_lst):
    if i == 5:
        continue
    print(i)
def sum(a,b):
    return(a+b)
sum = sum(2,3)
print(sum)

s1="Hello"
print(s1.strip())
print(s1.lower())
print(s1.upper())
print(s1.find("ee"))
print(s1.replace(" geetha ","Geetha"))
list=[1,2,3]
list.append(2)
print(list)
numbers=[1,2]
print(numbers[1])
print(numbers[0:2])
print(len(numbers))
print(2 in numbers)
l1=[1,2,3,4]
l2=[4,3,2,4]
print(l1+l2)
l1.extend([2,3])
print(l1)
l1.insert(4,8)
print(l1)
l1.pop(3)
print(l1)
print(l1.index(3))
l1.reverse()
print(l1)
l1.sort()
print(l1)
s1={1,2}
s5={2,3}
s6={3,4}
s7={7,8,4}
print(s1.union(s5,s6,s7))
l={1,2,3,4}
l.clear()
print(l)
set1={1,2,3,4,5,2}
set2={2,3,6,8,3,4,9}
print(set1 | set2)
set1={1,2,3,4}
set2={1,2,3,4,5,6,74,56}
print(set2.union(set1))

