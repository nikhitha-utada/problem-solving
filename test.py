# def min(my_list):
#     min = my_list[0]
#     for i in range(0,len(my_list)):
#        if my_list[i]<min:
#            min = my_list[i]
#     return min
# my_list = [2,8,1,9,7,3,6,4]
# first_min = min(my_list)
# my_list.remove(first_min)
# second_min = min(my_list) 
# print(second_min)    

str = "nikhitha"
my_list=[]
for i in range(0,len(str)):  
    count=1
    for j in range(i+1,len(str)): 
        char = str[i]
        if char == str[j] and char not in my_list:
            count+=1
            print(char,":",count)
            my_list.append(char)
# print(my_list)
    

        


















