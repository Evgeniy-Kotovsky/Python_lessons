while True:
    x = int(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    y = int(input("Enter second number: "))

    if operation == "+":
        result = x + y
        print(result)
    elif operation == "-":
        result = x - y
        print(result)
    elif operation == "*":
        result = x * y
        print(result)
    elif operation == "/":
        if y == 0:
            print("ERROR!!!")
        else:
            result = x / y
            print(result)


    again = input("Do you want to continue? (y/n): ")
    if again == "n":
        print("End")
        break