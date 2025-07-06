x = int(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
y = int(input("Enter second number: "))
if operation == "+":
    result = x + y
    print(result)
if operation == "-":
    result = x - y
    print(result)
if operation == "*":
    result = x * y
    print(result)
if operation == "/":
    if y == 0:
      print("ERROR!!!")
    else:
      result = x / y
      print(result)



