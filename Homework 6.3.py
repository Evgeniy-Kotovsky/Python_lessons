def multiply_digits_until_single(num):
    while num > 9:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
    return num
number = int(input("Enter number: "))
result = multiply_digits_until_single(number)
print(result)