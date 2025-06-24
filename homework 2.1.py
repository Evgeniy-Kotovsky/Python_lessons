number = int(input("Enter four numbers: "))

d1, rem1 = divmod(number, 1000)
d2, rem2 = divmod(rem1, 100)
d3, d4 = divmod(rem2, 10)

print(d1)
print(d2)
print(d3)
print(d4)

