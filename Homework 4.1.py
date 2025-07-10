lst = [0, 1, 0, 12, 3]
result = []
zero_count = 0
for num in lst:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1
result.extend([0] * zero_count)
print(result)

lst = [0]
if 0 in lst:
    lst.remove(0)
    lst.append(0)
print(lst)

lst = [1, 0, 13, 0, 0, 0, 5]
result = []
zero_count = 0
for num in lst:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1
result.extend([0] * zero_count)
print(result)

lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result = []
zero_count = 0
for num in lst:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1
result.extend([0] * zero_count)
print(result)
