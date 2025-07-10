import random
lenght = random.randint(3, 10)
lst = [random.randint(1, 50) for i in range(lenght)]
print(lst)
new_list = [lst[0], lst[2], lst[-2]]
print(new_list)
