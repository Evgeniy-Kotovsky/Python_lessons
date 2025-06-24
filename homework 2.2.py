number = int(input("Enter five nubmers: "))

d1, rem1 = divmod(number, 10000)
d2, rem2 = divmod(rem1, 1000)
d3, rem3 = divmod(rem2, 100)
d4, d5   = divmod(rem3, 10)

print(d5, d4, d3, d2, d1)
