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

