lst = [1, 2, 3, 4, 5, 6]
my_list1 = lst[:3]
my_list2 = lst[3:6]
my_list = [my_list1] + [my_list2]
print(my_list)

lst = [1, 2, 3]
my_list1 = lst[:2]
my_list2 = lst[-1:]
my_list = [my_list1] + [my_list2]
print(my_list)

lst = [1, 2, 3, 4, 5]
my_list1 = lst[:3]
my_list2 = lst[-2:]
my_list = [my_list1] + [my_list2]
print(my_list)

lst = [1]
my_list1 = lst[0]
my_list2 = lst[-1:0]
my_list = [my_list1] + [my_list2]
print(my_list)

lst =[]
my_list1 = lst[-1:]
my_list2 = lst[-1:]
my_list = [my_list1] + [my_list2]
print(my_list)






